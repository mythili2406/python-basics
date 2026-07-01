"""Problem Statement---

Write a Python program to generate the multiplication table of a given number without using the multiplication (*) operator.

The program should:

Read the table number from the user.
Read the starting multiplier.
Read the ending multiplier.
Calculate each multiplication result using successive addition only.
Display the multiplication table from the starting multiplier to the ending multiplier."""

table=int(input("enter a value:"))
start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))
while start<=end:
 result = 0
 count = 1

 while count <=start:
    result  +=  table
    count += 1

 print(f"{table}x{start} ={result}")
 start+=1