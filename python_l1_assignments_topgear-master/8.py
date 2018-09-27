#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("bookstore.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print "Root element : %s" % collection.getAttribute("shelf")

# Get all the movies in the collection
books = collection.getElementsByTagName("book")

# Print detail of each movie.
for book in books:
   print "\n"
   if book.hasAttribute("category"):
      print "Category: %s" % book.getAttribute("category")

   title = book.getElementsByTagName('title')[0]
   print "Title: %s" % title.childNodes[0].data
   author = book.getElementsByTagName('author')[0]
   print "Author: %s" % author.childNodes[0].data
   year = book.getElementsByTagName('year')[0]
   print "Year: %s" % year.childNodes[0].data
   price = book.getElementsByTagName('price')[0]
   print "Price: %s" % price.childNodes[0].data
