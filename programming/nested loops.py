#to make box
rows = int(input("enter the # of rows "))
cols = int(input("enter the # of columns "))
char = input("enter the character to make a box out of")

for c in range (rows):
 
 for x in range(cols):
      print (char, end="")
 print()