class Book:
    author = ''
    title  = ''

    def __init__(self, author,title):
        self.author = author
        self.title  = title

    def display(self):
        print('%s, written by %s'%(self.title,self.author))

john = Book('John Steinbeck','Of Mice and Men')
lee  = Book('Harper Lee','To Kill a Mockingbird')
john.display()
lee.display()
