import json

with open("books.json", "r") as f:
    data = json.load(f)

while True:
    bookTitle = input("Enter book title or type exit to quit: ")
    if bookTitle.lower() == "exit":
        print("Goodbye")
        break

    bookFound = False
    for book in data["books"]:
        if book["title"].lower() == bookTitle.lower():
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year Published: {book['year']}")
            print(f"Availability: {book['available']}")
            bookFound = True
            break
    if not bookFound:
        print("Couldn't find book!")



