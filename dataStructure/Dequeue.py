class Node:
    __data = None;
    __next_p = None;

    def __init__(self):
        pass;

    @property
    def data(self):
        return self.__data

    @property
    def next_p(self):
        return self.__next_p

    @data.setter
    def data(self, data):
        self.__data = data

    @next_p.setter
    def next_p(self, data):
        self.__next_p = data


class Dequeue:

    __head = None
    __tail = None

    def __init__(self):
        pass;

