str="hello"

rev=""

stlen=len(str)

for i in range(stlen):
    rev=str.charAt(i) + rev
    
print(rev)    
