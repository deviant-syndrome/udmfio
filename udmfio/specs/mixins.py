class PropertyMixin:
    def __init__(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)

