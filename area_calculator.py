#calculator practicing classes, methods, functions
import math

class Shape:
    #allows creation of Shape object, which can have base, height, side, radius, or combination of any of these characteristics (set to zero if not applicable)
	def __init__ (self, base = 0, height = 0, side = 0, radius = 0):
		self.base = base
		self.height = height
		self.side = side
		self.radius = radius
    
    #will set the dimensions based on the shape choice
	def get_dimensions(self, shape_choice): 
		if shape_choice == 1: #rectangle
			self.base = float(input("Enter the length of the base: "))
			self.height = float(input("Enter the height of the rectangle: "))
		elif shape_choice == 2: #square
			self.side = float(input("Enter the length of the side of the square: "))
		elif shape_choice == 3: #triangle
			self.base = float(input("Enter the length of the base of the triangle: "))
			self.height = float(input("Enter the height of the triangle: "))
		elif shape_choice == 4: #circle
			self.radius = float(input("Enter the radius length of the circle: "))
		elif shape_choice == 5: #parallelogram
			self.base = float(input("Enter the length of the base: "))
			self.height = float(input("Enter the height (perpendicular to the base): "))
	
    #will calculate and print the area of the shape choice
	def get_area(self, shape_choice):
		if shape_choice == 1: 
			area = self.base * self.height
			print(f"\nThe area of the rectangle is {area}")
		elif shape_choice == 2: 
			area = self.side * self.side
			print(f"\nThe area of the square is {area}")
		elif shape_choice == 3: 
			area = (1/2) * self.base * self.height
			print(f"\nThe area of the triangle is {area}")
		elif shape_choice == 4: 
			area = math.pi* (self.radius)**2
			print(f"\nThe area of the circle is {area}")
		elif shape_choice == 5:
			area = self.base * self.height
			print(f"The area of the parallelogram is {area}")


#allow a user menu selection:
another_calc = True
while another_calc == True:
    print("\nPlease select the shape: \n1)Rectangle \n2)Square \n3)Triangle \n4)Circle \n5)Parallelogram \n6)Quit Program\n")
    shape_choice = int(input("Enter the number you would like to select here: "))
    print("")

    if shape_choice>=1 and shape_choice <=5: #the user selected to quit the program
        user_shape = Shape() #creates a new shape with no dimensions!
        user_shape.get_dimensions(shape_choice) 
        user_shape.get_area(shape_choice)
    elif shape_choice == 6:
        another_calc = False
    else:
        print("Invalid input. Please enter a value of 1-4:")

#TODO- try/catch for typing out shape name instead of int in input