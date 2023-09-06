class UDMFMap:
    def __init__(self):
        self.linedefs = []
        self.vertexes = []
        self.sidedefs = []
        self.sectors = []
        self.things = []
        # Add more lists for other map components as needed

    def add_linedef(self, linedef):
        self.linedefs.append(linedef)

    def add_vertex(self, vertex):
        self.vertexes.append(vertex)

    def add_sidedef(self, sidedef):
        self.sidedefs.append(sidedef)

    def add_sector(self, sector):
        self.sectors.append(sector)

    def add_thing(self, thing):
        self.things.append(thing)

    # Add more methods for adding other map components as needed
