p= 0
r= 0
t=0
while p <=0 :
    p = float(input("enter the principle"))
    if p <= 0 :

       print("principle cant be o or less")
print(f" the principle is {p}")
while r <=0 :
  r = float(input("enter the rate"))
  if r <= 0 :

       print("rate cant be o or less") 
print(f" the rate is {r}")

while t <=0 :
    t = float(input("enter the time in years"))
    if p <= 0 :

       print("time cant be o or less")
print(f" the time is {t}")

cp = p*pow((1 + r/100),t)
print(f"the compound interest would be ${cp}")

