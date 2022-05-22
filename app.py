from models import (Base, session,
                    Book, engine)
import datetime
import csv


def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1. Add book
        \r2. View all books
        \r3. Search for book
        \r4. Book analysis
        \r5. Exit''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
            \rPlease choose one of the options above.
            \rA number from 1 - 5.
            \rPress Enter to try again.''')

# add books to the db
# edit books
# delete books
# search function
# data cleaning


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)


def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)


def app():
    app_running = True
    while app_running:
        choice = menu()

        # this is slow... refactor to use an indexed dict obj.
        if choice == '1':
            '''add book'''
            pass
        elif choice == '2':
            '''view books'''
            pass
        elif choice == '3':
            '''search book'''
            pass
        elif choice == '4':
            '''book analysis'''
            pass
        else:
            '''exit'''
            print('GOODBYE')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # app()
    # add_csv()
    clean_date('October 25, 2017')
