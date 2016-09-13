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
    __f_node=None;

    def add(self, data):
        node=Node();
        node.data=data;
        node.next_p=self.__head;

        if node.next_p is None:
            self.__f_node=node;

        self.__head=node;
        self.__f_node.next_p=self.__head;

    def getList(self):
        cur=self.__head;
        tmpCur=self.__head;

        while cur.next_p != tmpCur:
            print(cur.data);
            cur=cur.next_p;
        print(self.__f_node.data);

    def size(self):
        cur=self.__head;
        tmpCur=cur;
        l_size=0;

        while cur.next_p != tmpCur:
            l_size+=1;
            cur=cur.next_p;

        l_size+=1;

        return l_size;

    def search(self, data):
        ind=0;
        cur=self.__head;
        l_size=(self.size())-1;

        while ind<=l_size:
            if cur.data==data:
                return tuple([ind, cur.data]);
            else:
                cur=cur.next_p;
                ind+=1;

        if ind>l_size:
            return "not found data : %d" %data;

    def remove(self, ind):
        


def main():
    cll=ChainLinkedList();
    cll.add(3);
    cll.add(100);
    cll.add(52);
    cll.add(30);
    cll.add(203);

    #cll.getList();

if __name__ == "__main__":
    main();