from dataclasses import dataclass


@dataclass
class Items:
    name: str
    amount: int
    value: float


inventory = [Items]


def create_entry() -> None:
    print('')
    name = str(input('Name: '))
    amount = str(input('Amount: '))
    value = str(input('Value: $'))
    print('')
    with open('inventory.txt', 'a') as f:
        f.write(f"""{name}\n""")
        f.write(f"""{amount}\n""")
        f.write(f"""{value}\n""")


def update_file() -> None:
    print('')
    name = input('Name: ')
    new_name = input('New Name: ')
    amount = input('Amount: ')
    value = input('Value: $')
    counter = 0
    with open('inventory.txt', 'r') as f:
        inventory = f.readlines()
        for entry in inventory:
            if entry == str(f"""{name}\n"""):
                inventory[counter] = (f"""{new_name}\n""")
                inventory[counter + 1] = (f"""{amount}\n""")
                inventory[counter + 2] = (f"""{value}\n""")
            counter += 1
    with open('inventory.txt', 'w') as f:
        f.writelines(inventory)


def search_file() -> None:
    print('')
    name = input('Name: ')
    print('')
    entry_exists = False
    counter = 0
    with open('inventory.txt', 'r') as f:
        inventory = f.readlines()
        for entry in inventory:
            if entry == str(f"""{name}\n"""):
                print(
                    f"""Name: {inventory[counter]}Amount: {inventory[counter+1]}Value: {inventory[counter+2]}"""
                )
                entry_exists = True
            counter += 1
    if entry_exists == False:
        print('Entry does not exist')


def print_file() -> None:
    counter = 0
    print('')
    with open('inventory.txt', 'r') as f:
        inventory = f.readlines()
        for entry in inventory:
            if counter % 3 == 0:
                print(
                    f"""Name: {inventory[counter]}Amount: {inventory[counter+1]}Value: {inventory[counter+2]}"""
                )
            counter += 1


def delete_entry() -> None:
    print('')
    name = input('Name: ')
    print('')
    counter = 0
    with open('inventory.txt', 'r') as f:
        inventory = f.readlines()
        for entry in inventory:
            if entry == str(f"""{name}\n"""):
                inventory.pop(counter + 2)
                inventory.pop(counter + 1)
                inventory.pop(counter)
            counter += 1
    with open('inventory.txt', 'w') as f:
        f.writelines(inventory)


def main() -> None:
    while True:
        print('[create] [update]\n[search] [all]\n[delete] [quit]\n')
        action = input('>')
        if action == 'create':
            create_entry()
        elif action == 'update':
            update_file()
        elif action == 'search':
            search_file()
        elif action == 'all':
            print_file()
        elif action == 'delete':
            delete_entry()
        elif action == 'quit':
            break
        else:
            print('Input a valid action')


if __name__ == '__main__':
    main()
