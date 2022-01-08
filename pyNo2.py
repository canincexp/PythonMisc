docput=input('please enter doc path or doc name if it is in the same folder \n')
fhand=open(docput,encoding='utf-8')
inp=fhand.read()

print("system will show the text till that word")
nput=input('please enter the word \n')

n=inp.find(nput)
d=int(n)
print(inp[:d])
print('hello added')
