
#here the code for multiple choice by using for loop        

while True:

    choice = input('''

1 for Addition
2 for Subtration
3 for Multiplication
4 for Division
Please choose the operation: ''')

    if choice == '1':
        x = input("For 1st value: ")
        y = input('For 2nd value: ')
        z=int(x)+int(y)
        print("The Addition of ", x, " and ",y ," is ", z)

    elif choice == '2':
        x = input("For 1st value: ")
        y = input('For 2nd value: ')
        z=int(x)-int(y)
        print("The Subtration of ", x, " and ",y ," is ", z)        

    elif choice == '3':
        x = input("For 1st value: ")
        y = input('For 2nd value: ')
        z=int(x)*int(y)
        print("The Multiplication of ", x, " and ",y ," is ", z)

    elif choice == '4':
        x = input("For 1st value: ")
        y = input('For 2nd value: ')
        z=int(x)/int(y)
        print("The Division of ", x, " and ",y ," is ", z)

    else:
        print('''
Sorry. Wrong input.''')
