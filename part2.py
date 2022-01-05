"""
******
PART 2
******
Write a program that asks the user to enter a positive integer n. The program will then print the sum of the first n positive cubes.

For example, if the user types in 4, the program should print 100 (since 1^3 + 2^3 + 3^3 + 4^3 = 100).
"""

#write your code here
num = int(input("Enter a positive integer: "))

if num < 0: 
  print("That is not a valid input.")
  num = int(input("Enter a positive integer: "))

add = 0

for i in range(1, num+1):
  add = add + i**3

print(add)