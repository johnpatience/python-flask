import math

radius = float (input("Enter radius of the sphere: "))
height =float (input("Enter height of the sphere: "))

volume = math.pi * radius**2 * height
Surface_Area = 2 * math.pi * radius(height + radius)

print(f"Volume of the cylinder = {volume:.2}")
print(f"Area of the cylinder = {Surface_Area:.2}")
