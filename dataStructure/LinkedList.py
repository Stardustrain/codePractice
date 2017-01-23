class Node:
    def __init__(self):
        self.next_p = None
        self.data = None


class LinkedList:

    def __init__(self):
        self._num_of_size = 0
        self._head = None

    def add(self, data):
        self._num_of_size += 1
        node = Node()
        node.data = data

        if self._head is None:
            self._head = node
        else:
            node.next_p = self._head
            self._head = node

    def _remove_node(self, remove_node, prev_node):
        prev_node.next_p = remove_node.next_p

    def remove(self, data):
        if self._head.data == data:
            self._num_of_size -= 1
            self._head = self._head.next_p
        else:
            cur = self._head
            while cur is not None:
                if cur.next_p.data == data:
                    self._num_of_size -= 1
                    remove_node = cur.next_p
                    prev_node = cur
                    self._remove_node(remove_node=remove_node,
                                      prev_node=prev_node)
                    break
                else:
                    cur = cur.next_p

    def reverse(self):
        prev = None
        cur = self._head

        while cur is not None:
            next_node = cur.next_p
            cur.next_p = prev
            prev = cur
            cur = next_node

        self._head = prev

    def get_list(self):
        cur = self._head
        while cur is not None:
            print(cur.data)
            cur = cur.next_p

    def size(self):
        return self._num_of_size


def main():
    ll=LinkedList();
    ll.add(3);
    ll.add(52);
    ll.add(42);
    ll.add(72);
    ll.add(100);
    ll.add(120);
    ll.remove(120)
    ll.reverse()
    ll.get_list()
    print("size : {}".format(ll.size()))
    '''
    print("+++++++++++++++++++++++++")
    '''
    # ll.reverse();
    # ll.getList()

if __name__=="__main__":
    main();

