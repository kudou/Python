import math

def area_triangle(side1, side2, side3):
	"""Returns the area of a triangle with the given side lengths."""
	
	# Uses Heron's formula
	s = (float(side1) + side2 + side3) / 2
	return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print area_triangle(3, 4, 5)
