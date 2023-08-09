#print('Hello SoftUni')

# a = int(input())
# b = int(input())
#
# area = a * b
# print(area)

# x =  int(input("please enter an integer: "))
# if x< 0:
#     x=0
#     print("Negative changed to zero")
# elif x == 0:
#     print('Zero')
# elif x==1:
#     print('Single')
# else:
#     print("More")

words = ['cat','dog','racoon','horse','fox']
# for w in words:
#     print(w,len(w))
#
# for i in range(5):
#     print(i)
#
# for i in range(len(words)):
#     print(i,words[i])

# for num in range(2,10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number",num)

# while True:
#     pass
#
# point = (0,3)
# match point:
#     case (0,0):
#         print("Origin")
#     case (0,y):
#         print(f"Y={y}")
#     case (x,0):
#         print(f"X={x}")
#     case (x,y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")

# creating small app for calculation area

import math

def calculate_square_are(side):
    return side ** 2
def calculate_rectangle_are(length,width):
    return length * width
def calculate_circle_are(radius):
    return math.pi  * radius ** 2
def main():
    print("Welcome to the area calculator!")
    print("1. Calculate the area of square.")
    print("2. Calculate the area of a rectangle.")
    print("3. Calculate the area of a circle.")

    choice = input("Enter your choice [1, 2 or 3]: ")

    if choice == "1":
        side = float(input("Enter the length of the side: "))
        area = calculate_square_are(side)
        print(f"The are of the square is: {area}")
    elif choice == "2":
        length = float(input("Enter the length of the side: "))
        width = float(input("Enter the width of the side: "))

        area = calculate_rectangle_are(length, width)
        print(f"The area of the reactangle is: {area}")
    elif choice == "3":
        radius = float(input("Enter the radius: "))
        area = calculate_circle_are(radius)

        print(f"The radius of the circle is: {area}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
