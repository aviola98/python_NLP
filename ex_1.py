infile = open("qbdata.txt","r")

#print(infile.read())

for line in infile:
    values = line.split()
    print(values[0],values[1],'teve valor',values[10])

infile.close()