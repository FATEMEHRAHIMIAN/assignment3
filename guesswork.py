from ast import Num
from random import random
import random

input("keep number in your mind in range  \n" )

count = 1 
a = 0
b = 99
while count!= 0:
    Num = random.randint(a,b)   
    print("my guess is " , Num )
    tmp = input( "your number than my guess is \t lower ? \t or \t larger ? \t or \t true? \n"  )
    if tmp == "lower":
        b = Num - 1
        a = a
        count = count + 1
      
    elif tmp == "lorger":
            a = Num + 1
            b = b
            count = count + 1

    elif tmp =="true":
        print("Well done to me!")
        print ("my guess is qual to your number:) \n",count, "times")
        break
