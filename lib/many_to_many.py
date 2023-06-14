class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [n for n in Contract.all if n.author == self]
    
    def books(self):
        return [n.book for n in Contract.all if n.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        sum = 0
        sumlist = [n.royalties for n in Contract.all if n.author == self]
        for i in sumlist:
            sum += i
        return sum
        


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [n for n in Contract.all if n.book == self]
    
    def authors(self):
        return [n.author for n in Contract.all if n.book == self]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def get_author(self):
        return self._author 
    
    def set_author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    def get_book(self):
        return self._book
    
    def set_book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception

    def get_date(self):
        return self._date
    
    def set_date(self, date):
        if type(date) == str:
            self._date = date
        else:
            raise Exception
        
    def get_royalties(self):
        return self._royalties
    
    def set_royalties(self, royalties):
        if type(royalties) == int:
            self._royalties = royalties
        else:
            raise Exception
    
    author = property(get_author, set_author)
    book = property(get_book, set_book)
    date = property(get_date, set_date)
    royalties = property(get_royalties, set_royalties)

    # This is what the Instructions ask for the contracts_by_date method to do:
    # @classmethod
    # def contracts_by_date(cls, date):
    #     return [(n.book.title, n.date) for n in Contract.all if n.date == date]

    # This is what the Test asks for the contract_by_date method to do:
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key= lambda n: n.date)

        


# mica = Author("Mica Lee")
# june = Author("June Deltson")
# tides = Book("The Work Beneath the Tideline")
# swell = Book("Dorset Island Swells")
# sand = Book("The Sandstorm")
# natural = Book("The True Nature of Lester's Collection")

# mica.sign_contract(tides, "Oct 12", 35)
# mica.sign_contract(swell, "Feb 9", 32)
# june.sign_contract(sand, "May 18", 27)
# june.sign_contract(natural, "May 18", 28)

# print(mica.name)
# print([n.title for n in mica.books()])
# print(june.name)
# print([n.title for n in june.books()])
# print([f"{n.name}'s total royalties: {n.total_royalties()}" for n in Author.all])
# print([n.book.title for n in Contract.all])
# print([(n.book.title, n.date) for n in Contract.contracts_by_date()])