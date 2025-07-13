# My Calculator
print('------------------ Use Calculator ---------------------------')
a = int(input("enter num1 : "))
b = int(input("enter num2 : "))
print("1 for add \n2 for sub\n3 for mul\n4 for div")
a1 = int(input())
match a1:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)