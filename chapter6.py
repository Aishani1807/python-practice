'''a1=int(input("Enter a no.:"))
a2=int(input("Enter a no.:"))
a3=int(input("Enter a no.:"))
a4=int(input("Enter a no.:"))
if(a1>a2 and a1>a3 and a1>a4):
    print(a1,"is the greatest no.")
elif(a2>a1 and a2>a3 and a2>a4):
    print(a2,"is the greatest no.")
elif(a3>a1 and a3>a2 and a3>a4):
    print(a3,"is the greatest no.")
else:
    print(a4,"is the greatest no.")

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
comment=input("Enter your comment:")
if ((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("This comment is a spam")
else:
    print(comment)

username=input("Enter your username:")
if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("Username identified")

l=eval(input("Enter a list:"))
name=input("Enter a name:")
if name in l:
    print("Name found")
else:
    print("Your name is not in the list")

marks=int(input("Enter your marks:"))
if (marks>=90 and marks<=100):
    print("Ex")
elif (marks>=80 and marks<90):
    print("A")
elif (marks>=70 and marks<80):
    print("B")
elif (marks>=60 and marks<70):
    print('C')
else:
    print('F')'''

post=input("Enter your post")
if ('Harry' in post):
    print("Post contains Harry")
else:
    print("Post does not contain Harry")






