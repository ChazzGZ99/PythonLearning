#Variables

my_variable = "Mi variable de String"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)   
print(my_int_variable)
print(type(my_int_to_str_variable))

#Concatenacion de vartiables
print(my_variable, str(my_int_variable) , my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

#Monstruo de print type
print(type(print(my_variable, str(my_int_variable) , my_bool_variable)))

#Funciones del Sistema
print(len(my_int_to_str_variable))
print(len(my_variable))

#Variables en una sola linea
name, surname, alias, age = "Carlos", "Gastelum", "Chazz", 23
print("Mi nombre es ",name,"Mi apellido es " ,surname, "Mi alias es ",alias, "Mi edad es ",age)

first_name = input("Cual es tu nombre?")
edad =input("Cual es tu edad?")

#Forzar el tipo
address: str = "Mi direccion"
address = 32
print(type(address))