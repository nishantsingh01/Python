def length_str():
    str = input("Enter the string: ")
    print("Length of string: ", len(str))

def maximum_of_three():
    str1 = input("Please Enter 1st String: ")
    str2= input("Please Enter 2nd String: ")
    str3 = input("Please Enter 3rd String: ")
    maxstr = ""
    if str1 > str2 and str1 > str3:
        maxstr = str1
    elif str2 > str1 and str2 > str3:
        maxstr = str2
    else:
        maxstr = str3
    print("Maximum is: ", maxstr)

def replace_vowels():
    str = input("Enter the string: ")
    new_str = ""
    vowels = ['a','e','i','o','u']
    for i in range(0, len(str), 1):
        if str[i].lower() in vowels:
            new_str += "#"
        else:
            new_str += str[i]
    print("Replaced string: ", new_str)

def numofwords():
    str = input("Enter the string: ")
    str = str.strip() + " "
    count = 0
    for i in range(0, len(str), 1):
        if str[i] == " ":
            count += 1
    print("No of words: ", count)

def palindrome():
    str = input("Enter the string: ")
    new_str = ""
    for i in range(0, len(str), 1):
        new_str = str[i] + new_str
    if str == new_str:
        print(f"{str} is a palindrome.")
    else:
        print(f"{str} is not a palindrome")

def main():
    print("\n Menu:")
    print("Press 1 for Finding Length of the string")
    print("Press 2 for Finding the Maximum of three strings")
    print("Press 3 for Replacing the Vowelsb with '#'")
    print("Press 4 for the No. of Words")
    print("Press 5 for Checking whethere String is Palindrome or NOT")
    print("Press 6 for Exit")
    option = input("Your choice: ")

    switcher = {
        '1' : length_str,
        '2' : maximum_of_three,
        '3' : replace_vowels,
        '4' : numofwords,
        '5' : palindrome,
        '6' : quit
    }
    func = switcher.get(option, lambda: print("Error!! Please Select from the Options"))
    func()

if __name__ == "__main__":

    ch = 'y'
    while ch.lower() == 'y':
        main()
        ch = input("\nDo you Want to Use Once more? [y/n]: ")
