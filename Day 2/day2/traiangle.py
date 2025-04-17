import math

# Function to calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

# Function to check if the triangle is isosceles
def is_isosceles(distances):
    # Check if any two distances are equal (isosceles property)
    return distances[0] == distances[1] or distances[1] == distances[2] or distances[0] == distances[2]

# Function to check if the triangle is right-angled
def is_right_angled(distances):
    # Sort the distances to easily find the largest one (hypotenuse)
    distances.sort()
    # Check if Pythagorean theorem holds
    return math.isclose(distances[0]**2 + distances[1]**2, distances[2]**2)

# Main function to check both properties
def check_triangle_type(A, B, C):
    # Calculate the distances between each pair of points
    dAB = distance(A, B)
    dBC = distance(B, C)
    dCA = distance(C, A)

    # Store distances in a list
    distances = [dAB, dBC, dCA]

    # Print distances
    print(f"Distance AB: {dAB}")
    print(f"Distance BC: {dBC}")
    print(f"Distance CA: {dCA}")
