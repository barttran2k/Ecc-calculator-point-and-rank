from findpoint import get_points
from rankP import get_rank
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
        get_points()
    elif choice == 2:
        print('Find rank of a point')
        get_rank()
    elif choice == 3:
        print('Exit')
        exit()
    else:
        print('Invalid choice')
