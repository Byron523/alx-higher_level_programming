#!/usr/bin/python3
class Square():
    def __init__(self, size=0, position=(0, 0)):
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        x = self.__size
        if x == 0:
            print()
        else:
            for i in range(x):
                for j in range(x):
                    print("#", end='')
                print('$')
