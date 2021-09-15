infile = open("qbdata.txt","r")

#print(infile.read())

#read each line of the file 
for line in infile:
    #split the line in values
    values = line.split()
    #print the first and second value of each line and the last one
    #first and secon value = name
    #last value = rating of each athlete
    print(values[0],values[1],'teve valor',values[10])

infile.close()