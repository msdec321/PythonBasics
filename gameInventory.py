#This is a video game inventory script.

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1,
    'arrow': 12}


def displayInventory(invent):

    item_count=0
    print('Inventory')
    for k, v in invent.items():
        print(v, k)
        item_count+=v

    print('Total number of items:', item_count)


displayInventory(inventory)
