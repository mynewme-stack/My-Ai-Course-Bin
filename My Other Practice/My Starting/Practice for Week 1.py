book_title = "Think and Grow Rich"
book_price = 45.5
author = "Napoleon Hill"
book_year = 2025
print( "Book Title: ",book_title, type(book_title))
print("Book Price: ",book_price, type(book_price))
print("Author: ",author, type(author))
print("Year: ",book_year, type(book_year))
percentage = (book_price * 10) / 100
print(percentage)
book_price = book_price + 5
book_price += 5
print(book_price)
book_description = book_title + " is execelent book. I have read it multiple times. "
print(book_description)
print(book_title[15::])
print(len(book_title))
for i in book_title:
    print(i)
age = int(input("Please enter your age: "))
if age > 10:
    print("Greater!")


