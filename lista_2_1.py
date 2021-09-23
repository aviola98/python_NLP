#create a string called "instituto de ciências matemáticas e de computação"
string = "instituto de ciências matemáticas e de computação"
print(string)

#add usp 

string  = string + " usp"
print(string)

#add 2021

string = string + " 2021"
print(string)

#verify the length of the new string

len(string)

#convert string to upper case

string = string.upper()
print(string)

#convert string to lower case

string = string.lower()
print(string)

#remove white space from either the beginning or the end

string  = string.strip()
print(string)

#replace all 'a' wiht 'x'

string = string.replace("a","x")
print(string)

#split the string

lista = string.split()
print(lista)

#verify length

len(lista)

#string string using 'de' as separator

string_de = string.split("de")
print(string_de)

#verify length

len(string_de)

#join the splitted strings

string_junto = " ".join(lista)
print(string_junto)
string_de_junto = " ".join(string_de)
print(string_de_junto)

#join the spĺitted strings using '/'

string_barra = "/".join(lista)
print(string_barra)
string_de_barra  = "/".join(string_de)
print(string_de_barra)