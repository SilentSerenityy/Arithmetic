from serv import serveron
serveron()

import random
import time
import math

while True:
  x = int(input("Enter in a number! : "))
  y = int(input("Enter in another number! : "))

  if x > y:
    print("\nPlease redo this sequence again, making number one smaller than number two! This is for the range function, so it can work properly.\n")
  
  else:
    break

a = x + y   #the sum of and x and y
b = x - y   #the difference of x and y
c = x * y   #product from x and y
d = x / y   #quotient of x and y
e = x // y  #floor division quotient of x and y
f = x ** y  #x to the power of y
g = x % y   #modulo of x and y
h = random.randint(x , y)


print("\nAnalyzing...")
time.sleep(2)
print("\nHere is the analyzation of the numbers you have provided!\n")
print("The sum of your two numbers is:\t",x,"+",y,"=",a,"\n")
print("The difference of your two numbers is:\t",x,"-",y,"=",b,"\n")
print("The multiplication of your two numbers is:\t",x,"*",y,"=",c,"\n")
print("The quotient of your two numbers is:\t",x,"/",y,"=",d,"\n")
print("The quotient in floor division of your two numbers is:\t",x,"//",y,"=",e,"\n")
print("When your two numbers were randomly ranged, the number that was picked from",x,"to",y,"was:\t",h,"\n")
print("When you two numbers were moduled by modulo, the remainder was:\t",g)
#simple and very general number analysis

while True:
  z = input("\nWould you like to see what your two numbers put to the power of each other was? It has been hidden because the number would be way too large to show... \t")

  if z == "yes":
    print("\nWhen",x,"was put to the power of",y,"it equaled:\t",x,"**",y,"=",f,"\n")
    break
  
  elif z == "no":
    print("\nAlright! You have chosen to not see",x,"to the power of",y,".")
    break
  
  else:
    print("\nYou have entered an invalid response... please try again.")

time.sleep(3)

print("\nAlright, let us insert some values into Quadratic Equations!\nA Qaudratic Equation goes as such:\t x = -(b) ± √(b)² + 4(a)(c)/ 2(a)\n")
#this was quite a doozy copying and pasting the individual parts of this equation, such as the positive/negative sign, squared symbol, and square root symbol

print("I will let you take this in for a while, so you can try to understand this.")
time.sleep(5)
print("\nWhy don't you put some numbers in?")

xx = int(input("\nWhat would you like 'a' to be equal to? : "))
yy = int(input("What would you like 'b' to be equal to? : "))
zz = int(input("What would you like 'c' to be equal to? : "))

aa = -yy          #this would be negative b
bb = yy * yy      #this would be b to the power of two
cc = 4 * xx * zz  #this would be 4(a)(c)
dd = 2 * xx       #this would be 2(a)
ee = bb + cc      #simplifying the equation more so
ff = math.sqrt(ee)

print("\nProcessing...\n")
time.sleep(3)

print("Alright, we have plugged in the given variables and simplified the equation. This is what we have:\tx =",aa,"± √",ee,"/",dd,"\n")
print("The sqaure root of",ee,"is:\t",ff)
#I'll need to finish from these
