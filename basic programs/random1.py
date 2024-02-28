'''import random
n = random.randbytes(3)
print(n)

print(random.randrange(1,8))

print(random.randint(100,211))
mylist=("Jadeja","Ashwin","Rahane","Shami","dhoni","virat")
mylist1={"Jadeja","Ashwin","Rahane","Shami","dhoni","virat"}
print(random.choice(mylist))
print(random.shuffle(mylist))'''



import string
import random
S=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=S))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran1)