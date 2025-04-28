import xml.dom.minidom

domtree = xml.dom.minidom.parse('books.xml')
group = domtree.documentElement
books = group.getElementsByTagName('book')

def searchBooks(titleToFind):
    for book in books:
        #print(f"-- Book {book.getAttribute('title')} --")
        title = book.getElementsByTagName('title')[0].childNodes[0].nodeValue
        if title.lower() == titleToFind.lower():
            author = book.getElementsByTagName('author')[0].childNodes[0].nodeValue
            year = book.getElementsByTagName('year')[0].childNodes[0].nodeValue
            available = book.getElementsByTagName('available')[0].childNodes[0].nodeValue

            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Year: {year}")
            print(f"Available: {available}")

    print(f"'{titleToFind} is not available!")


while True:
    bookTitle = input("Enter book title or type exit to quit: ")

    if bookTitle.lower() == 'exit':
        print("Goodbye!")
        break

    searchBooks(bookTitle)




