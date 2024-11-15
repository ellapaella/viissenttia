class Refrence:
    def __init__(self, id):
        self.id = id
        # This is the class data structure. create one self.variable for each data field in the refrence

    def __str__(self):
        pass


class Article:
    def __init__(self,author,title,journal,year,volume,number,pages):
        self.author=author
        self.title=title
        self.journal=journal
        self.year=year
        self.volume=volume
        self.number=number
        self.pages=pages