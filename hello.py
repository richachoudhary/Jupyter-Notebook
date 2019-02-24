# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:40:16 2019

@author: RICHA
"""
def printhello (x):
    print(x)


printhello("my name is ")
printhello("richa")

#fucntion to  test wheather a number os prime or not 

def isprime (x):
    for i in range (2,x):
        if(x%i==0):
            print('not a prime num')
            break
        else :
            print('is a prime num')
            break
        
        
isprime(17)
isprime(20)

class city:
	name = "Sharjah"

	def info(self, new_name): # note that the first argument is self
		self.name = new_name # access the class attribute with the self keyword

x = city()

x.info("Dubailand")

print(x.name)




class city(object):
	citizen = 'EMIRATES'

	def __init__(self, name, country):
		self.name = name
		self.country = country

x = city(name='Dubai', country = 'UAE')
print(x.name, x.country, x.citizen)


class carkhareedna (object):
    headofthefamily= 'papa' #here define that attribute which will remain constant through out
    
    def __init__(self, familymemberswhocandrive, familymembershavetolearnfirsttodrive):
        self.familymemberswhocandrive= familymemberswhocandrive
        self.familymembershavetolearnfirsttodrive= familymembershavetolearnfirsttodrive
       
y= carkhareedna(familymemberswhocandrive= 'papa', familymembershavetolearnfirsttodrive= 'shivam richa')
print(y.headofthefamily, y.familymemberswhocandrive, y.familymembershavetolearnfirsttodrive )


class Circle(object):
	pi = 3.14

	def __init__ (self, radius=1):
		self.radius = radius
	def area (self):
		return Circle.pi * self.radius * self.radius
	def setRadius(self,radius):
		self.radius = radius
	def getRadius(self):
		return self.radius

c = Circle()
c.setRadius(24)

print('Radius is', c.getRadius(), '& Area is', c.area())


#Create a class 'Book' with special methods str, len, & del.
class Book(object):
	def __init__(self, title, author, pages):
		print('A Book is created.')
		self.title = title
		self.author = author
		self.pages = pages
	def __str__(self):
		return "Title: %s, Author:%s, Pages:%s " %(self.title, self.author, self.pages)
	def __len__(self):
		return self.pages
	def __del__ (self):
		print ('A book is destroyed')

#On initiating or instantiating an object of class 'Book', init method will be called by default.
sub = Book('Who moved my cheese', 'Unknown', 200)





print(sub)


class Student(object):
	def __init__(self):
		print('Student is created.')
	def whoami(self):
		print('Student')
	def course(self):
		print('Learning')

class Subject(Student):
	def __init__(self):
		Student.__init__(self)
		print('Subject is Created')
	def whoami(self): #Again defining the method overrides its parent class method
		print('Subject')
	def chapter(self):
		print('Inheritance')

subs = Subject()
subs.chapter()
print(subs.course())


class Person:
	def __init__(self, first, last, age):
		self.firstname = first
		self.lastname = last
		self.age = age

	def __str__(self):
		return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):
	def __init__(self, first, last, age, staffnum):
        
		super().__init__(first, last, age)
		self.staffnumber = staffnum

	def __str__(self):
		return super().__str__() + ", " + self.staffnumber

x = Person("Marge", "Simpson", 36)
y = Employee("Homer", "Simpson", 28, "1007")

print(x)
print(y)

str('Adam')
print(str('10'))
class vehicle:
    def __init__(self, milege, acceleration, brakes):
        self.mileges= milege
        self.accelerations= acceleration
        self.brakess= brakes
        
    def __str__(self):
        return str(self.mileges) +" "+ str(self.accelerations)+ " "+ str(self.brakess)
    
        
        
class suzuki(vehicle):
    def __init__(self, milege, acceleration, brakes, speed, color):
        super().__init__(milege, acceleration, brakes)
        self.speeds= speed
        self.colors= color
        
    def __str__(self):
        return super().__str__()+", "+ str(self.speeds)+ " "+ str(self.colors)
    
    
s= vehicle("45", "45", 'brakesclucth')
r= suzuki("45", "46", 'newbeakrs', "199", "red")

print(s)
print(r)
        

























