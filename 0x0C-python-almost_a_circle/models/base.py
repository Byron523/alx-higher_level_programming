#!/usr/bin/python3
""" A class module called base """
import json
import csv
import turtle
import os


class Base:
    """

    Base class that is a base

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ An init method that instatiate args """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ a method that returns JSON string rep
        Args:
           item1: dictionary item
        """
        s = "[]"
        if list_dictionaries is None or list_dictionaries == []:
            return (s)
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ This method writes the JSON string rep of list_objs 2 file
        Args:
            cls: a class method
           list_objs: list objects
        """
        empty = cls.__name__ + ".json"
        with open(empty, "w") as outfile:
            if list_objs is None:
                outfile.write("[]")
            else:
                list_objs = [o.to_dictionary() for o in list_objs]
                outfile.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ A method that returns a list of json """
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ a class method that returns an instance
        Args:
            object: a double pointer dictionary
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """ A method that returns a list of instances """
        outfile = str(cls.__name__) + ".json"
        try:
            with open(outfile, "r") as jsonfile:
                dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ A CSV serialization method from list to a file
        Args:
            list_objs(list): list inherited
        """
        outfile = cls.__name__ + ".csv"
        with open(outfile, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field = ['id', 'width', 'height', 'x', 'y']
                else:
                    field = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csvfile, field=field)
                for item in list_objs:
                    writer.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        outfile = cls.__name__ + ".csv"
        try:
            with open(outfile, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]
                else:
                    field = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, field=field)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ This method Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
