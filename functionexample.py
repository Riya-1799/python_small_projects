#Write a function called calculate_area that takes base and height as an input
# and returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height

def calculate_area(base, height, shape="triangle"):
    if shape == "triangle":
        area = (1 / 2) * base * height
    elif shape == "rectangle":
        area = base * height
    else:
        print("Shape is neither triangle nor rectangle")
        return None  # Return None if the shape is invalid
    return area  # Return the calculated area

# Example usage
area1 = calculate_area(10, 5)  # Default is triangle
print(f"Area of triangle is: {area1}")

area2 = calculate_area(10, 5, "rectangle")
print(f"Area of rectangle is: {area2}")

area3 = calculate_area(10, 5, "circle")  # Invalid shape
print(f"Invalid shape result: {area3}")