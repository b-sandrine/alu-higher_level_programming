#!/usr/bin/python3
""" Thhis module contains class called rectangel """


class Rectangle:
    """ Defining a class Rectangle with 2 attributes height and width"""

    number_of_instances = 0   # Public class attribute
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantitiating the attributes """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # Getters and setter for the 2 attributes
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Area of rectangle
    def area(self):
        return self.width * self.height

    # Perimiter of rectangle
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    # __str__ function to print the string representation of the rectange
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(
                str(self.print_symbol) * self.width for _ in range(self.height)
                )

    # __repr__ function to  should return a string representation
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    # Detecting if an instance is deleted
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # A static function for returning the biggest rectangle
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # Checking which one has the biggest area
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    # Class method that defines a rectangle
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
