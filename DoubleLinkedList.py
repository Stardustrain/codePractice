class Node:
    __data=None;
    __next_p=None;
    __prev_p=None;

    def __init__(self):
        pass;

    @property
    def data(self):
        return self.__data;

    @property
    def next_p(self):
        return self.next_p;

    @property
    def prev_p(self):
        return self.__prev_p;

    @data.setter
    def data(self, data):
        self.__data=data;

    @next_p.setter
    def next_p(self, next_p):
        self.__next_p=next_p;

    @prev_p.setter
    def prev_p(self, prev_p):
        self.__prev_p=prev_p;


class DoubleLinkedList:
    __head=None;
    __cur_node=None;
    __tail=None;

    def __init__(self):
        pass;

    def add(self, data):
        node=Node();
        node.data=data;
        node.next_p=self.__head;
        self.__head=node;
