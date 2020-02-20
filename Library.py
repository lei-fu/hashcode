class Library:
    def __init__(self, books, duration, limits):
        self.books = books
        self.duration = duration
        self.limits = limits
    def __str__(self):
        s = ""
        for i in self.books:
            s += str(i) + " "
        s += str(self.duration) + " " +  str(self.limits)
        return s