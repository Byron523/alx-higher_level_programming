#!/usr/bin/python3
""" A class module called base """
import json


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
    def load_from_csv(cls):
        """ Method that loads a CSV file """
        filee = "{}.csv".format(cls.__name__)

        if os.path.exists(filee) is False:
            return []

        with open(filee, 'r') as outfile:
            reader = csv.reader(outfile)
            csv_l = list(reader)

        if cls.__name__ == "Rectangle":
            l_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            l_keys = ['id', 'size', 'x', 'y']

        matrix = []
        for item in csv_l:
            my_dict = {}
            for i in enumerate(item):
                my_dict[l_keys[i[0]]] = int(i[0])
            matrix.append(my_dict)

        lis = []
        for item in range(len(matrix)):
            lis.append(cls.create(**matrix[index]))

        return (lis)
