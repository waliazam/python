'''
To open a file, you use the open() function. 
This function requires the path to your file as a mandatory argument and returns a file object.
Optionally, you can specify the mode in which the file should be opened, like 'r' for reading, 
'w' for writing, 'a' for appending, 'r+' for both reading and writing, etc. 
If no mode is specified, 'r' (read) mode is assumed by default.

'''

file = open('Mytext.txt', 'r')

content = file.read()

print(content)