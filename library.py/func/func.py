import time
import json
library= []
jsonfilename = 'librarys.json'
def save_books_to_json(book, file_path):
    with open(file_path, 'w') as file:
        json.dump({"book": library}, file, indent=2)
# Function to load the list of books from a JSON file
def load_books_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['book']

def addBook():
    new_book = {}
    new_book["name"] = input("name of the new book: ")
    new_book["author"] = input("author of the new book: ")
    new_book["genre"] = input("genre of the new book: ")
    library.append(new_book)
    print("loading...")
    time.sleep(2)
    print("Book added")
    save_books_to_json(library, jsonfilename)
    main()

def removeBook(booktodelete):
    for i in range(len(library)):
        if library[i]["name"] == booktodelete:
            del library[i]
            break
    time.sleep(2)
    print("Removing Done")
    save_books_to_json(library, jsonfilename)
    main()

def getBook():
    library=load_books_from_json(jsonfilename)
    for i in range(len(library)):
        time.sleep(1)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Name:" + library[i]["name"])
        print("Author:" + library[i]["author"])
        print("Genre:" + library[i]["genre"])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    main()

def help():
    print("================================")
    print("Write add to add a new book to your library")
    print("Write delete to remove the book from your library")
    print("Write show to show the library")
    print("================================")
    main()

def main():
    command = input("Your Command: ")
    if 'help'in command:
        help()
    if 'show' in command:
        getBook()
    if 'delete' in command:
        word = command.split() 
        word = word[1]
        removeBook(word)
    if 'add' in command:
        addBook()
    else:
        print("Invalid command, Type 'help' for more information")
        main()