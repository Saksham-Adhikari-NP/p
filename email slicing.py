email = input("enter your email ")
index = email.index("@")
username = email[:index]
domain = email[index+1:]
print(f"ur user name is {username} and domain is {domain}")