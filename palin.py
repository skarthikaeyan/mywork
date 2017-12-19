#!/usr/bin/python3
class  cap:
    def __init__(self):#creating constructor
        self.a="" #initializing variables
    def chck(self):#created class chck
        self.a = input("Enter a string: ")
        self.a = self.a.replace(" ","")  #removing spaces
        self.a=self.a.replace('\'',"")
        print(self.a)
        self.a=str(self.a.upper())  #converting to upper case
        return self.a

class palin(cap): #inherited from cap class
    def palincheck(self):
        self.x=self.a  #using base class member a
        self.x2=reversed(self.x) #reversing the string
        if(list(self.x)==list(self.x2)): #to check both the list matches
            print("Palindrome")
        else:
            print("not palindrome")
while True:
    b=palin()
    b.chck()
    b.palincheck()
    c=input("contine y/n?")
    c=c.upper()
    if(c=='Y'):
        continue
    else:
        break