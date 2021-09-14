import sqlite3
from quotes import Quote
from parser import *

conn = sqlite3.connect("quotes_database.db")
conn.text_factory = str

c = conn.cursor()

# c.execute("""CREATE TABLE quotes (
#     quote text,
#     author text
#     )""")

# def insert_q(quote) : 
#     with conn :
#         c.execute("INSERT INTO quotes VALUES (:text, :author)", {'text': quote.text, 'author': quote.author})

# def get_quote_by_aut(author) : 
#     c.execute("SELECT * FROM quotes WHERE author=:author", {'author': author})
#     return c.fetchall()

# def update_txt(quote, text) : 
#     with conn :
#         c.execute("""UPDATE quotes SET text=:text WHERE author=:author""", {'text': text, 'author': quote.author})

# def update_aut(quote, author) : 
#     with conn :
#         c.execute("""UPDATE quotes SET author=:author WHERE text=:text""", {'text': quote.text, 'author': author})

# def remove_aut(quote) :
#     with conn :
#         c.execute("DELETE from quotes WHERE first=:first AND last:=last", {'text': quote.text, 'author': quote.author})

# def extract_empty(lines) : 
#     for line in lines : 
#         if line == "" :
#             lines.remove(line)
#     return lines

# def index_authors(lines) :
#     author_indices = []
#     for i in range(0, len(lines)) : 
#         if (lines[i])[0:2] == "--" : 
#             author_indices.append(i)
#     return author_indices

# def get_quotes() : 
#     with open("quotes.txt", 'r') as q:
#         lines = q.readlines()
#         lines = extract_empty(lines)
#         author_indices = index_authors(lines)
#         curQuote = ""
#         quotes = {}
#         for i in range(0, len(lines)) : 
#             if i not in author_indices : 
#                 curQuote += lines[i].strip() + " "
#             else : 
#                 curAuthor = lines[i][2:].strip()
#                 if curAuthor not in quotes:
#                     quotes[curAuthor] = []
#                 quotes[curAuthor].append(curQuote)
#                 curQuote = ""
#         return quotes

# quotes = get_quotes()

# for author in quotes.keys() : 
#     for q in quotes[author] : 
#         insert_q(Quote(q, author))

# quotes = get_quote_by_aut("Mark Twain")
# print(quotes)

conn.close()