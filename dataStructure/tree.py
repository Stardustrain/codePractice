class Node:

    __key = None
    __data = None
    __left_p = None
    __right_p = None

    def __init__(self):
        pass

    @property
    def key(self):
        return self.__key

    @property
    def data(self):
        return self.__data

    @property
    def left_p(self):
        return self.__left_p

    @property
    def rigth_p(self):
        self.__right_p


    @key.setter
    def key(self, data):
        self.__key = data

    @data.setter
    def data(self, data):
        self.__data = data

    @left_p.setter
    def left_p(self, data):
        self.__left_p = data

    @right_p.setter
    def right_p(self, data):
        self.__right_p = data


class Tree:
    def __init__(self):
        pass

    