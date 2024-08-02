# lst = [1,32,3,4,2,34,43,34,24,56,54,75,30]

# # help ("sorted")
# # a = lst.sort
# # print (lst [:4])
# print(lst [2:6])

# ----------------------------------------
# import numpy as np 
# from numpy import random

# a = random.randn(3,2)
# print (a)

# b = random.randn(3,2)
# print (b)

# c = random.randint(10, size=10)  
# print (c)

# d = random.randint (10 , size=(2,6)) 
# print (d)
# -------------------------------------------

# x = [1,23,24,21,512,35,654,685,345,6,98,79,34,52]

# for i in x:
#     print (x)

# ----------
# x= ["apple","banana", "kiwi"]
# for i in x:
#     print (x)
# --------------
# # Loop a string
# for i in "banana":
#     print (i)
# ------------------------------------------------------------------------------------------------
# program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# a = input("Enter your name: ")
# age= int(input("Enter your age: "))

# cal = 2024 - age +100
# year = str(cal)

# print (f"hi {a}, your age is {age}, and you will be 100 yrs old in {year}")
# ------------------------------------------------------------------------------------------------
# Program to check whether number is even or odd

# num = int(input("Enter a number to check it is even or odd : "))

# cal = num % 2

# if cal>0:
#     print ("The number is odd")
# else:
#     print ("The number is even")
# --------------------------------------------------------------------------------------------------
# write a program that prints out all the elements of the list that are less than 10.


# lst = [1,32,3,4,2,34,43,34,24,56,54,75,30,2,32,43,36,33,52,32,323,2,32]


# new = []
# for i in lst:
#     if i > 10:
#         # new.append(i)
#         # print (i)
#         # new = []
#         new.append(i)
#         lst.sort()
# print(new)
# print (lst)

# # To get the list number which are smaller then given number 
# num= int(input("Give a number: "))
# for i in lst:
#     if i<num:
#         print(i)

# a= lst.count(32)  #-----------------------  To count the occurence of the elements
# print (a)

# for i in (lst):
#     print (i)
# -----------------------------------------------------------------------------------------------

# asks the user for a number and then prints out a list of all the divisors of that number.


# num = int(input("Enter the number to check whether its divisor or not: "))
# lst1 = []

# for i in list(range (1,num+1)):
#     if num%i==0:
#         lst1.append(i)
# print (lst1)


#-------------Practice ----------------------
# num = int (input("Enter the number to check the divisors : "))
# lst = []

# for i in list(range(1, num+1)):
#     if num%i==0 :
#         lst.append(i)
# print (lst)


# x=int(input("num:"))
# y=[]
# for num in list(range(1,x+1)):
# if x%num==0:
# y.append(num)

# print(y)

# -------------------------------------------------------------------------------------------------

# lst = [1,32,3,4,2,34,43,34,24,56,54,75,30,2,32,43,36,33,52,32,323,2,32]

# a= [21,3,31,["alpha"]]

# lst.append(a)
# # print (lst)

# lst.insert()


# --------------------------------------------------------------------------------7
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird


# n = int (input ("Enter number: "))

# cal = n%2
# if cal ==1 :
#     print ("Weird")
# elif 2<= cal <=5:
#     print ("Not Weird")
# elif 6 <= cal <=20:
#     print ("Weird")
# else :
#     print ("Not Weird")

# --------------------------------------------------------------------------------------------  Division and Float division

# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  a//b .
#  The second line should contain the result of float division,  a/b .

# No rounding or formatting is necessary.

# Example
# a =3
# b =5
# The result of the integer division 3//5 = 0.
# The result of the float division is 3/5 = 0.6.

# a = int(input("Enter number for a: " ))
# b = int (input("Enter number for b: "))

# c = a//b
# d =round(a/b,6)

# print (f"he result of the integer division{a}//{b} is :{c}")
# print (f"he result of the integer division{a}/{b} is :{d}")

# ---------------------------------------------------------------------------------------------------
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.


# a = int(input("Enter number a :"))
# b = int(input("Enter number a :"))
# c = int(input("Enter number c :"))

# print (a+b)
# print (a-b)
# print (a*c)

# ----------------------------------------------------------------------------------------------------










# -----------------------------------------------------For Pattern 
# def search(pattern, text):
#     M = len(pattern)
#     N = len(text)
#     for i in range(N - M + 1):
#         j = 0
#         while j < M:
#             if text[i + j] != pattern[j]:
#                 break
#             j += 1
#         if j == M:
#             print(f"Pattern found at index {i}")
# search("ABCD", "ABCDABCDABCDABCD")


#-----------------------------------TO PRINT A HEART SHAPE--------------------------------
# from turtle import *
# bgcolor ("black")
# color("red")
# begin_fill()
# pensize (3)
# left(50)
# forward(134)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()
# -----------------------------------------------------------------------------------------

# from turtle import *
# forward (100)
# left(120)
# forward (100)
# right (120)
# ---------------------------------------False O/P
# print (0.1+0.2 == 0.3)
# -------------------------------------
# Set converted to a list and returns value
# Set didn't allow duplicate values

# s = {1,2,1,2,4,4,5,3}
# x = list (s)
# print (x[2])
# ---------------------------------------------

# lst1 = [20,30,40,60]
# lst2 = [20,30,40,60]

# print (lst1 == lst2)   # O/P = True
# print (lst1 is lst2)   # O/P = False

# ------------------------------------------------------

# def fun1(num):
#     return num+25

# fun1(5)
# print (num)   #O/P = Gives the Name Error

# -------------------------------------------------------------------------



# from ursina import*
# app =Ursina()
# me = Animation (
#     'assets\player',
#     Collider = 'box',y=5
# )
# Sky()
# camera.orthographic=True
# camera.fov = 20

# Entity (
#     model = 'quad',
#     Texture= 'assets\BG',
#     scale = 36, z=1
# )
# fly = Entity(
#     model='cube',
#     Texture='assets\\fly1',
#     Collider='box',
#     scale = 2, x= 20,y= -10
# )

# flies = []
# def newFly():
#     new = duplicate(
#         fly,
#         y=5+(5124*time.dt)%15
#     )
#     flies.append(new)
#     invoke(newFly,delay=1)
# newFly()

# def update():
#     for fly in flies:
#         fly.x -= 4*time.dt
#     me.y += held_keys ['w']*6*time.dt 
#     me.y -= held_keys ['s']*6*time.dt 
#     a = held_keys ['w']*-20
#     b = held_keys ['s']*20
#     if a!=0:
#         me.rotation_z= a
#     else:
#         me.rotation_z= b
#     for fly in flies:
#         fly.x -= 4*time.dt 
#         touch =fly.intersects()
#         if touch.hit():
#             flies.remove(fly)
#             destroy(fly)
#         t = me.intersects()
#         if t.hit and t.entity.scale==2:
#             quit()


# def input (key):
#     if key == 'space':
#         e= Entity(
#             y=me.y,
#             x=me.x+2,
#             model = 'cube',
#             Texture = 'assets\Bullet',
#             Collider = 'cube'
            
#         )
#         e.animate_x(
#             30,
#             duration = 2,
#             curve = curve.linear
#         )
#         invoke(destroy,e,
#                delay=2)

# app.run()


# ---------------------------------   Game (Throwing error)

# from ursina import*
# app =Ursina()
# me = Animation (
#     'assets\player',
#     Collider = 'box',y=5
# )
# Sky()
# camera.orthographic=True
# camera.fov = 20

# Entity (
#     model = 'quad',
#     Texture= 'assets\BG',
#     scale = 36, z=1
# )
# fly = Entity(
#     model='cube',
#     Texture='assets\\fly1',
#     Collider='box',
#     scale = 2, x= 20,y= -10
# )

# flies = []
# def newFly():
#     new = duplicate(
#         fly,
#         y=5+(5124*time.dt)%15
#     )
#     flies.append(new)
#     invoke(newFly,delay=1)
# newFly()

# def update():
#     for fly in flies:
#         fly.x -= 4*time.dt
#     me.y += held_keys ['w']*6*time.dt 
#     me.y -= held_keys ['s']*6*time.dt 
#     a = held_keys ['w']*-20
#     b = held_keys ['s']*20
#     if a!=0:
#         me.rotation_z= a
#     else:
#         me.rotation_z= b
#     for fly in flies:
#         fly.x -= 4*time.dt 
#         touch =fly.intersects()
#         if touch.hit():
#             flies.remove(fly)
#             destroy(fly)
#         t = me.intersects()
#         if t.hit and t.entity.scale==2:
#             quit()


# def input (key):
#     if key == 'space':
#         e= Entity(
#             y=me.y,
#             x=me.x+2,
#             model = 'cube',
#             Texture = 'assets\Bullet',
#             Collider = 'cube'
            
#         )
#         e.animate_x(
#             30,
#             duration = 2,
#             curve = curve.linear
#         )
#         invoke(destroy,e,
#                delay=2)

# app.run()

# -------------------------------------------------------------------------

# lst =  [3,4,5,6,7] 

# for i in lst:
#     lst.remove(i)
# print (lst)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#List comprehension  (expression - loop - condition

lst = [i for i in range (1,11) ]
lst

lst = [i**2 for i in range (1,11) ]  # to sqare the outcomes
lst

lst = [i+10 for i in range (1,11) if i%2 ==0 ]  # data which is devisible by 2
lst

lst = [i+10 for i in range (1,11) if i%2 ==0 ]  # data which is devisible by 2
lst

lst = [i+10 for i in range (1,11) if i%2 !=0 ]
lst













