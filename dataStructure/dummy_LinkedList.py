class Node:
    data = None
    next_p = None

    def __init__(self):
        pass


class LinkedList:
    head = None
    tail = None
    _numOfSize = 0

    def __init__(self):
        self.dummy = Node()
        self.head = self.dummy
        self.tail = self.dummy

    def add(self, data):
        self._numOfSize += 1
        node = Node()
        node.data = data
        self.tail.next_p = node
        self.tail = node

    def get_list(self):
        cur = self.head.next_p

        while cur is not None:
            print(cur.data)
            cur = cur.next_p

    def search(self, val):
        cur = self.head.next_p
        ind = 0

        while cur is not None:
            if cur.data != val:
                cur = cur.next_p
                ind+=1
            else:
                return (ind, cur.data)
        return False

    def remove(self, val):
        cur = self.head.next_p
        before = self.head

        while cur is not None:
            if cur.data != val:
                before = cur
                cur = cur.next_p
            else:
                before.next_p = cur.next_p
                ret = cur.data
                del cur
                self._numOfSize -= 1
                return ret
        return False

    def length(self):
        return self._numOfSize


def main():
    ll = LinkedList()
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.remove(5)
    ll.get_list()
    ll.length()


if __name__ == "__main__":
    main()
