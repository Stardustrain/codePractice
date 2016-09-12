class Node:
    __data=None;
    __next_p=None;

    def __init__(self):
        pass;

    @property
    def data(self):
        return self.__data;

    @property
    def next_p(self):
        return self.__next_p;

    @data.setter
    def data(self, data):
        self.__data=data;

    @next_p.setter
    def next_p(self, next_p):
        self.__next_p=next_p;


class ChainLinkedList:
    __head=None;
    __tail=None;

    def __init__(self):
        pass;

    def add(self, data):
        node=Node();
        node.data=data;
        node.next_p=self.__head;
        self.__head=node;

    def getList(self):
        cur=self.__head;

        while cur != None:
            print(cur.data);
            cur=cur.next_p;


def main():
    cll=ChainLinkedList();
    cll.add(3);
    cll.add(100);
    cll.add(52);
    cll.add(30);
    cll.add(203);

    cll.getList();

if __name__ == "__main__":
    main();