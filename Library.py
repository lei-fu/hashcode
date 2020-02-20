class Library:
    def __init__(self, id, books, duration, limits):
        self.id = id
        self.books = books
        self.duration = duration
        self.limits = limits
        self.output = []
        self.score = 0

    def __str__(self):
        s = ""
        for i in self.books:
            s += str(i) + " "
        s += str(self.duration) + " " +  str(self.limits)
        return s
