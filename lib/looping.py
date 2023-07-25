#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i >0 :
      print(i)
      i -=1
      i == 1
      print( "Happy New Year!")


def square_integers(int_list):
    # code goes here!
    return [num **2  for num  in int_list]
   

def fizzbuzz():
    # code goes here!
     x= 1
     while x <= 100:
        if  x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")    
        elif  x % 5 == 0:
            print("Buzz") 
        else:
            print(x)
        x+=1 
   

