x = input("請輸入年分: ")
x = int(x)

def is_leap(x):
    x = int(x)
    if x % 4 != 0:
        return False
    elif x % 4 == 0 and x % 100 != 0:
        return True
    elif x % 100 == 0 and x % 400 != 0:
        return False
    elif x % 400 == 0 and x % 3200 != 0:
        return Ture

r = is_leap(x)
print(r)