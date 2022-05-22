from models import (Base, session,
                    Book, engine)

# import models
# main menu - add, search, analysis, exit, view options
# add books to the db
# edit books
# delete books
# search function
# data cleaning
# loop runs program


if __name__ == '__main__':
    Base.metadata.create_all(engine)
