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
        print(self.__head.data);
        self.__head=self.__head.next_p;
        self.remove(self.__head);

    def remove(self, d_node):
        d_node.next_p=None;
        del d_node;

    def isEmpty(self):
        pass;


def main():
    st=Stack();
    st.push(5);
    st.push(20);
    st.pop();
    st.getStack();
if __name__=="__main__":
    main();