file = open("text.txt" , 'w')

content = file.write("THis is the text for write filie")


file.close()


with open('text.txt', 'r') as file:
    content = file.read()
    print(content)

# The file is automatically closed outside of the with block
