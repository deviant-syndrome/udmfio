import re


# "data/extensions/zdoom.txt
def read_extensions(file_path: str = None):
    with open(file_path, 'r') as f:
        extensions = f.read()
    extensions = extensions.split('\n')
    for idx, line in enumerate(extensions):
        line = line.strip()
        extensions[idx] = line
        if line.startswith('//'):
            extensions[idx] = ''

    return [line for line in extensions if line]


def find_extensions(extensions, class_name):
    class_begin = 0
    class_end = 0
    for idx, extension in enumerate(extensions):
        if extension == class_name:
            class_begin = idx
            rest = extensions[idx:]
            for idx2, line in enumerate(rest):
                if line.startswith('}'):
                    class_end = idx + idx2
                    break
    return extensions[class_begin + 2:class_end]


if __name__ == '__main__':
    with open("data/udmf.txt", 'r') as f:
        udmf_spec = f.read()

    extensions = read_extensions("data/extensions/zdoom.txt")
    extensions.extend(read_extensions("data/extensions/slade.txt"))
    spec = udmf_spec
    class_field_re = re.compile(r'\s*(\w+)\s*=\s*<(\w+)>;')

    class_defs = []
    current_class_lines = []

    spec_lines = spec.split('\n')
    for idx, line in enumerate(spec_lines):
        line = line.strip()
        if line.endswith('{'):
            current_class_lines.append(line)
            class_name = spec_lines[idx - 1].strip()
        elif line.startswith('}'):
            current_class_lines.append(line)
            class_def = '\n'.join(current_class_lines)
            class_defs.append((class_name, class_def))
            current_class_lines = []
        elif current_class_lines:
            current_class_lines.append(line)

    # Generate classes
    for class_name, class_def in class_defs:
        field_defs = class_def.split('\n')[1:-1]
        field_dict = {}

        init_args = []
        fields = []
        class_extensions = find_extensions(extensions, class_name)
        for extension in class_extensions:
            field_defs.append(extension)

        for field_def in field_defs:
            match = class_field_re.match(field_def)

            if match:
                field_name, field_type = match.groups()
                if field_name in field_dict.keys():
                    print(f"Using extension field {field_name} in class {class_name}")
                    continue
                field_dict[field_name] = field_type
                init_args.append(f"{field_name}=None")  # todo: default values for different types
                fields.append(f"self.{field_name} = {field_name}")

        parent_class = class_name.capitalize()  # Assuming the parent class name is capitalized
        init_args_str = ", ".join(init_args)
        fields_str = "\n        ".join(fields)
        class_template = f"""from .mixins import PropertyMixin


class {parent_class}(PropertyMixin):
    def __init__(self, {init_args_str}):
        {fields_str}
        super().__init__(kwargs={{
            {", ".join([f"'{field}': self.{field}" for field in field_dict])}
        }})
        """
        class_template = class_template.replace("{class_name}", class_name)
        class_template = class_template.replace("{parent_class}", parent_class)
        class_template = class_template.replace("{init_args}",
                                                ", ".join([f"'{field}': {field}" for field in field_dict]))
        class_template = class_template.replace("{fields}", fields_str)
        with open(f"{class_name}.py", 'w') as f:
            f.write(class_template)
