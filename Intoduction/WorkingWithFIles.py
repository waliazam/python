import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
shelfFile.close()