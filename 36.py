class Publisher:
  def __init__(self,name1):
     self.name=name1
  def show(self):
    pass
class Book(Publisher):
  def __init__(self,title1,author1,name1):
    self.title=title1
    self.author=author1
    Publisher.__init__(self,name1)
  def show(self):
   pass
class Python(Book):
  def __init__(self,p,no,title1,author1,name1):
    self.price=p
    self.no_of_pages=no
    Book.__init__(self,title1,author1,name1)
  def show(self):
    print('Book title:',self.title)
    print('Author:',self.author)
    print('Publisher:',self.name)
    print('Price: Rs.',self.price)
    print('No of pages:',self.no_of_pages)
P1=Python(700,300,'Programming with Python','GV Rossum','ABC Books')
P1.show()