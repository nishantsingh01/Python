print("Enter a No. greater than or equal to 10:")
num = int(input())
if num >= 10:
    _set = set()
    while num != 0:
        _set.add(num%10)
        num = int(num/10)
    print("Set: ", _set)
else:
    print("Sorry! Number is less than 10")