import socket as s
website=input("Enter website :- ")
print("Website IP address is: ",s.gethostbyname(website))