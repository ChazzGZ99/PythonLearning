## STRINGS ##

my_string = "Mi string"
my_other_string = "mi otro sting"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

#salto de linea
my_new_line_string = 'este esun string \n con salto de linea'
print(my_new_line_string)

#tab
my_tab_string = "\tsto es una tab"
print(my_tab_string)

my_scape_string = "\tsto es un string \n escp"
print(my_scape_string)


#FORMATEO

name, subname, age= "Chazz", "GZ", 24
print("mi nombre es {} {} y mi edad es {}".format(name,subname,age))
print("mi nombre es %s %s y mi edad es %d" %(name,subname, age))
print(f"Mi nombre es {name} {subname} y mi edad es {age}")


#Desempaquetar caracteres
language = "python"
a, b, c, d, e, f = language

print(a)
print(e)

#Division

language_slice =language[1:3]
print(language_slice)

language_slice =language[1:]
print(language_slice)

#REVERSA

reversed_language = language [::-1]
print(reversed_language)

#Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print("1".isnumeric())
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())





