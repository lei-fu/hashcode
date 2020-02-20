class Reader():
    array = []
    next = -1
    
    def __init__(self, name):
        self.array =[]
        self.next = -1
        self.name = name
        with open(name, 'r') as f:
            for line in f: # read rest of lines
                self.array.extend([x for x in line.split()])
    
    def nextInt(self):
        self.next += 1
        return int(self.array[self.next])
    
    def nextFloat(self):
        self.next += 1
        return float(self.array[self.next])
