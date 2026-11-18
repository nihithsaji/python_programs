class Publisher:
    def __init__(self,name):
        self.name = name


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author


class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        print("Publisher:", self.name)
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Number of Pages:", self.pages)


p = Python("ABC Publishers", "Python Programming",
           "John Smith", 500, 250)
p.display()

