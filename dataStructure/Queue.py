class Node:

    __data = None;
    __next_p = None;

    def __init__(self):
        pass

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
    def next_p(self, next_p):
        self.__next_p = next_p


class Queue:

    __head = None;
    __cur_node = None;

    def __init__(self):
        pass

    def en_queue(self, data):
        node = Node()
        node.data = data
        if self.__head is None:
            self.__head = node
            self.__cur_node = node
        else:
            self.__cur_node.next_p = node
            self.__cur_node = node

    def de_queue(self):
        ret = self.__head
        self.__head = self.__head.next_p

        return ret

    def get_queue(self):
        cur = self.__head

        while cur is not None :
            print(cur.data)
            cur = cur.next_p

    def isEmpty(self):
        return True if self.__nead is None else False


def main():
    qu=Queue();
    qu.en_queue(5)
    qu.en_queue(6)
    qu.en_queue(7)
    qu.en_queue(8)
    qu.en_queue("last")

    qu.get_queue()

    qu.de_queue()

    print("===============")

    qu.get_queue()


if __name__ == "__main__":
    main()



