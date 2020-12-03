class InputToArray:
    def __init__(self, filename='input.txt', mode='string', delimiter='\n'):
        self.filename = filename
        self.mode = mode
        self.delimiter = delimiter

        self.array = []

        f = open(self.filename, 'r')
        self.array = f.read().split(self.delimiter)
        f.close()

        self.array = [x for x in self.array if x]

        if self.mode == 'int':
            self.array = [int(x) for x in self.array]
        if self.mode == 'float':
            self.array = [float(x) for x in self.array]
