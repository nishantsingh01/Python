import math

def calculate(s1, s2, s3):
    perimeter = 0
    area = 0
    # Check if input forms a triangle
    if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
        print("It's a Triangle, PERIMETER and AREA is:")
        perimeter = s1 + s2 + s3
        s = perimeter/2
        area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    else:
        print("Sorry!! The given sides doesn't form a Traingle")
        print("[Sum of two sides of a triangle should be greater than the third]")
        quit()
    return perimeter, area

if __name__ == "__main__":
    s1 = float(input("Enter the length of side 1: "))
    s2 = float(input("Enter the length of side 2: "))
    s3 = float(input("Enter the length of side 3: "))
    perimeter, area = calculate(s1, s2, s3)
    print("The Perimeter is",end=" : ")
    print(perimeter)
    format(perimeter)
    print("The Area is", end=(" : "))
    print(area)
    format(area)

