items = {'rope': 1, 'torch': 4, 'gold coin': 42, 'dagger': 1, 'arrow': 12}




def displayInventary(inventory):
    print('Inventary:')
    
    item_total = 0
    for k , v in inventory.items():
        print(str(v) + ' and ' + k)
        
        item_total += v
    print('The total is: ' + str(item_total))
displayInventary(items)