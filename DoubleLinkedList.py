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
        return self.__next_p;

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

        if node.next_p is None:
            self.__tail=node;
        else:
            self.__cur_node.prev_p=node;

        self.__head=node;
        self.__cur_node=node;

    def getList(self, rev=False):
        if rev is False:
            cur=self.__head;

            while cur is not None:
                print(cur.data);
                cur=cur.next_p;
        else:
            cur=self.__tail;

            while cur is not None:
                print(cur.data);
                cur=cur.prev_p;

    def search(self, data, rev=False):
        if rev is False:
            cur=self.__head;

            while cur is not None:
                if cur.data == data:
                    return cur;
                cur=cur.next_p;
            return "data [ %d ] not found" % data
        else:
            cur=self.__tail;

            while cur is not None:
                if cur.data == data:
                    return cur;
                cur=cur.prev_p;
            return "data [ %d ] not found" % data

    def remove(self, data, rev=False):
        if rev is False:
            cur=self.search(data, rev);
            rm=None;

            if self.__head.data==data:
                rm=self.__head;
                self.__head=rm.next_p;
                self.__head.prev_p=None;
                rm.next_p=None;
                del rm;

            else :

                cur=self.__head;
                while cur is not None:
                    if cur.data == data:
                        break;
                    cur=cur.next_p;

                if cur is self.__tail:
                    self.__tail=cur.prev_p;
                    cur.prev_p=None;
                    self.__tail.next_p=None;
                    del cur;

                else:
                    cur.prev_p.next_p=cur.next_p;
                    cur.next_p.prev_p=cur.prev_p;
                    del cur;

        else :
            cur=self.search(data, rev);

            if self.__tail.data==data:
                rm=self.__tail;
                self.__tail=rm.prev_p;
                self.__tail.next_p=None;
                rm.prev_p=None
                del rm;

            else:
                cur=self.search(data, rev);

                if cur is self.__head:
                    self__head=cur.next_p;
                    self__head.prev_p=None;
                    cur.next_p=None;
                    del cur;
                else:
                    cur.prev_p.next_p=cur.next_p;
                    cur.next_p.prev_p=cur.prev_p;
                    del cur;

def main():
    dll=DoubleLinkedList();
    dll.add(2)
    dll.add(10)
    dll.add(5)
    dll.add(30)
    dll.add(2)
    dll.add(7)
    dll.add(200)

    dll.remove(2, rev=False);
    dll.getList(rev=True);

if __name__=="__main__":
    main();
