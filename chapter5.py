words={"madad":"Help",
"kursi":"chair",
"billi":"cat"}
word=input("Enter the word you want the meaning of:")
print(words[word])

s=set()
for i in range(8):
    n=int(input("Enter number:"))
    s.add(n)
print(s)

q=set()
n=int(input("Enter a no."))
w=input("Enter a string")
q.add(n)
q.add(w)
print(q)

s={}
for i in range(4):
    name=input("Enter name:")
    lang=input("Enter language")
    s[name]=lang
print(s)
