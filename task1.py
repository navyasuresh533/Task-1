Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> my_list=[4,5,6,7,8,9]
>>> my_list.append(10)
>>> my_list.remove(6)
>>> my_list[0]
4
>>> print(my_list)
[4, 5, 7, 8, 9, 10]
>>> 
>>> my_dict={'name':'amal','age':'20','city':'goa'}
>>> my_dict['gender']='male'
>>> del my_dict['age']
>>> my_dict['city']='Banglore'
>>> print('update dictionary:',my_dict)
update dictionary: {'name': 'amal', 'city': 'Banglore', 'gender': 'male'}
>>> 
>>> my_set={1,2,3,4,5,6}
>>> my_set.add(7)
>>> my_set.remove(4)
>>> my_set.discard(3)
>>> my_set.add(10)
>>> print('updated set:',my_set)
updated set: {1, 2, 5, 6, 7, 10}
