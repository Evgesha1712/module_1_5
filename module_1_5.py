immutable_var = 1, 2.0, True, 'Hello'
print(immutable_var)
#immutable_var[0] = [5]
#print(immutable_var) #Код написан с ошибкой, поскольку в кортеже нельзя заменить один элемент на другой
mutable_list = [1, 'apple', 0.5, 'eggs' ]
mutable_list[2] = [4.5]
print(mutable_list)
