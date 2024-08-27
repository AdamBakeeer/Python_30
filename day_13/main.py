
language = 'Python'
lst = list(language) 
print(type(lst))     
print(lst)           


lst = [i for i in language]
print(type(lst)) 
print(lst)

numbers = [i for i in range(11)]
print(numbers)

even =[i for i in range(21) if i % 2 ==0]
print(even)

odd = [i for i in range(21) if i % 2 != 0]
print(odd)


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg = [i for i in numbers if i < 0]
print(neg)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
listt = [number for row in list_of_lists for sublist in row for number in sublist] 
print(listt)
