t = float(input("Write the  temp "))
u = input("write the unit k/c")
if u == "k":
    conv = t - 273
    print ( f" the temp converted to degree celcius is {conv} 'C ")
elif u == "c":
    
    conv = t + 273
    print ( f" the temp converted to degree celcius is {conv} 'K ")
else :
    print ( "this degree of measurement conbversion is not supported ")
    