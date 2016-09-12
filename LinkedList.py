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


class LinkedList:
    __head=None;

    def __init__(self):
        self.__head=None;

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

    def search(self, data):
        cur=self.__head;
        ind=0;
        while cur != None:
            if cur.data==data:
                return tuple([ind, cur.data]);
            else :
                cur=cur.next_p;

    def size(self):
        cur=self.__head;
        size=0;
        while cur != None:
            size+=1;
            cur=cur.next_p;

        return size;

    def remove(self, ind):
        cur=self.__head;
        prev=None;
        size=LinkedList.size(self);

        cnt=int(size-(ind+1))

        if cnt != 0:
            for i in range(cnt):
                prev=cur;
                cur=cur.next_p;

        if prev == None:
            self.__head=cur.next_p;
        else :
            prev.next_p=cur.next_p;

        cur=None;

    def reverse(self):
        cur=self.__head;
        f_node=cur;
        prev=cur;
        cur=cur.next_p;

        while cur != None:
            self.__head=cur;
            temp_p=cur.next_p;
            cur.next_p=prev;
            prev=cur;
            cur=temp_p;

        f_node.next_p=None;



def main():
    ll=LinkedList();
    ll.add(3);
    ll.add(52);
    ll.add(42);
    ll.add(72);
    ll.add(100);
    ll.add(120);
#    print("List struct")
#    ll.getList();
#    print("remove obj");
#    ll.remove(1);
#    ll.getList();
    '''
    ll.getList();
    print("+++++++++++++++++++++++++")
    '''
    ll.reverse();
    ll.getList()

if __name__=="__main__":
    main();