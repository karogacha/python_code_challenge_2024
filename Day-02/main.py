# Create a program to calculate the area of a circle given its radius.
import math

def circle_area(rad: float) -> float:
    return round(math.pi * (rad ** 2),ndigits=2)

def main():
    print("##### We will calculate the area of a circle given its radius. #####")
    radius = float(input("Enter the radius value:"))
    area = circle_area(radius)
    print(f"The resulting area is: {area}")

main()
