
Mightysho
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
More
alx-higher_level_programming/0x0A-python-inheritance/8-rectangle.py /
@Mightysho
Mightysho 0x0A-python-inheritance
 1 contributor
15 lines (11 sloc)  402 Bytes
#!/usr/bin/python3
'''task 8 module'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle class'''
    def __init__(self, width, height):
        '''Initialization of the object'''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
