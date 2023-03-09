def menu():
    print('---------------------Menu----------------------')
    print('1. Find points on the curve')
    print('2. Find rank of a point')
    print('3. Exit')
while True:
    menu()
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('Find points on the curve')
        from findpoint import *
    elif choice == 2:
        print('Find rank of a point')
        from rankP import *
    elif choice == 3:
        print('Exit')
        exit()
    else:
        print('Invalid choice')
