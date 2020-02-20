class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
    def __str__(self):
        return str(self.id) + " " +  str(self.score)
