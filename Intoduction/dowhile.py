birthdays = {'Wali': '3 Jan 2010', 'Laila': '4 Apr 1997', 'Sarah': '5 Jan 2010'}

# while True:
#     print("Enter you name: ")
#     name = input()
    
#     if name == '':
#         break
    
#     if  name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
        
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')
        
        
        
for i in birthdays.values():
    print(i)