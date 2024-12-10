crnum = "123-233-45-6245"
print(crnum[::2])
last_digit = (crnum[-4:])
print(f"XXX-XXX-XX-{last_digit}")
crnum = crnum[::-1]
print (crnum)