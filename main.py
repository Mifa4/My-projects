x = int(input("X:"))
y = int(input("X:"))
if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x > 0 and y < 0:
    print('IV')