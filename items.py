from abc import ABC
from datetime import date


class LibraryItem(ABC):
    """
    Abstract class for Book and CD.
    No instances should be created
    """

    def __init__(
        self,
        title: str,
        maker: str,
        ULR=None,
        isLoan: bool = False,
        dueDate: date = date.today(),
    ):
        self.__title = title
        self.__maker = maker

        # generate or assign a ULR
        # URL should be final
        if ULR:
            self.__ULR = ULR
        else:
            self.__ULR = str(abs(hash((title, maker))))

        self.__isLoan = isLoan
        self.__dueDate = dueDate

    # defining setters and getters

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getMaker(self):
        return self.__maker

    def setMaker(self, maker):
        self.__maker = maker

    def ULR(self):
        return self.__ULR

    def isLoan(self):
        return self.__isLoan

    def setLoan(self, loan):
        self.__isLoan = loan

    def getDueDate(self):
        return self.__dueDate

    def setDueDate(self, date):
        self.__dueDate = date

    def __str__(self):
        return f"{self.__title} by {self.__maker}, ULR: {self.__ULR}."

    def __repr__(self) -> str:
        return self.__str__()


class Book(LibraryItem):
    def __init__(
        self,
        title: str,
        author: str,
        ULR=None,
        isLoan: bool = False,
        dueDate: date = date.today(),
    ):
        super().__init__(title, author, ULR, isLoan, dueDate)

    def getAuthor(self):
        return self.getMaker()

    def setAuthor(self, author):
        return self.setMaker(author)


class CD(LibraryItem):
    def __init__(
        self,
        title: str,
        artist: str,
        ULR=None,
        isLoan: bool = False,
        dueDate: date = date.today(),
    ):
        super().__init__(title, artist, ULR, isLoan, dueDate)

    def getArtist(self):
        return self.getMaker()

    def setArtist(self, artist):
        return self.setMaker(artist)
