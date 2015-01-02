##places class

class Place(object):
    
    def __init__(self):
        self.filename = "goals.taskpaper"
        self.header = "48 Places:"
        self.parse_file()
        
    def parse_file(self):
        self.places = []
        self.file = open(self.filename, 'r')
        project = False
        for line in self.file:
            line = line.strip('\t\n ')
            if line and line == self.header:
                project = True
            elif line and line[-1] == ':':
                project = False
            elif line and project and line[0] == '-':
                self.places.append(line.strip('-'))
