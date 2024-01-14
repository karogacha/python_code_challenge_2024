# Create a program to calculate the area of a circle given its radius.
import math

def circle_area(rad: float) -> float:
    return round(math.pi * (rad ** 2),ndigits=2)

def main():
    print("##### We will calculate the area of a circle given its radius. #####")
    error = True
    while error:
        try:
            radius = float(input("Enter the radius value:"))
            error = False
        except ValueError as e:
            print("Only numeric values are valid. Please try again.")
        except Exception as e:
            print("An unexpected error ocurred while retreiving the value of radius. Please try again.")
    area = circle_area(radius)
    print(f"The resulting area is: {area}")

main()
