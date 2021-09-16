#create variables

a=1
b=5.9
c='test'

#returing type
print(type(a))
print(type(b))
print(type(c))

a = '1'
type(a)

b+c
#we can't sum two operators from different classes

lista = list(range(10))
lista

#add 6
lista.append(6)
lista

#add 7 in the third position of the list
lista[2]=7
lista

#remove the tird element of the list
lista.remove(7)
lista

lista.append(4)
lista

lista.count(4)

lista[:3]

lista[2:8]

lista[::3]

lista[-3:]

lista[:-4]

lista[6]

lista[7]=12
lista

lista[::-1]

lista[::1]

t = (0,1,2,3,4,5,6,7,8,9)

dicionario = {}
dicionario['kobayashi']= 'tohru'
dicionario['elma'] = 'food'
dicionario['lucoa'] = 'shouta'
dicionario['ilulu'] = 'taketo'
dicionario['fafnir']= 'takyia'
dicionario

for k in dicionario:
    print(k)

for k,v in dicionario.items():
    print(v)  

for k,v in dicionario.items():
    print(k,v)

print(list(dicionario.items())[1])   
print(dicionario)

for k,v in dicionario.items():
    print(k, 'tem valor',v)

outfile = open('numbers.txt','w')

for i in range(1,11):
    outfile.write(str(i)+'\n')

outfile.close()

infile = open('numbers.txt','r')
print(infile.readlines())

infile.close()

outfile = open('numbers.txt','w')
for i in range(11,21):
    outfile.write(str(i)+'\n')
outfile.close()

outfile = open('numbers.txt','a')
for i in range(21,30):
    outfile.write(str(i)+'\n')
outfile.close()

infile = open('numbers.txt','r')
for i in range(11,30):
    print(i)
infile.close()

infile = open('numbers.txt','r')
print(infile.readlines())
infile.close()
