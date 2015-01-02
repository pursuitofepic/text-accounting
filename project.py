#File with Class for parsing the Projects

class Project(object):
    
    def __init__(self):
        self.filename = "goals.taskpaper"
        self.header = "48 Projects:"
        self.parse_file()
        
    def parse_file(self):
        self.projects = []
        self.file = open(self.filename, 'r')
        project = False
        for line in self.file:
            line = line.strip('\t\n ')
            if line and line == self.header:
                project = True
            elif line and line[-1] == ':':
                project = False
            elif line and project and line[0] == '-':
                self.projects.append(line.strip('-'))
                