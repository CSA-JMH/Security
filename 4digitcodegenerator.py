import random
lit=[]
litter=[]
file=open("4digitcodes.txt","w")
while len(lit)<=100:
    x=random.randrange(1111,9999)
    if '0' in list(str(x)):
        x=random.randrange(1111,9999)
    elif x not in lit:
        lit.append(x)
    else:
        pass
lit=str(lit)
lit=lit.replace("[","")
lit=lit.replace("]","")
lit=lit.replace(" ","")
lit=lit.replace(",","\n")
file.write(lit)