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


class Stack:
    __head=None;

    def __init__(self):
        pass;

    def push(self, data):
        node=Node();
        node.data=data;
        node.next_p=self.__head;
        self.__head=node;

    def getStack(self):
        cur=self.__head;
        while cur is not None:
            print(cur.data);
            cur=cur.next_p;

    def peek(self):
        print(self.__head.data);

    def pop(self):
        ret = self.__head.data;
        del_node = self.__head
        self.__head = ret.next_p;
        self.remove(del_node);

        return ret

    def remove(self, d_node):
        d_node.next_p=None;
        del d_node;

    def isEmpty(self):
        return True if self.__head is None else False


def main():
    st=Stack();
    st.push(5);
    st.push(20);
    st.getStack()
    data=st.pop();
    print("pop : {data}".format(data=data))
    st.getStack();
    print(st.isEmpty())
if __name__=="__main__":
    main();