import unittest


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    # I added some modifications here to make it more flexible:
    # Returning removed item
    # Returning True/False if found or not found
    def remove(self, item, return_removed=False):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        if return_removed is True:
            return current
        return found

    def get(self):
        ret_arr = []
        current = self.head
        while current is not None:
            ret_arr.append(current.get_data())
            current = current.get_next()
        return ret_arr

    def append(self, item):
        temp = Node(item)
        current = self.head
        end = False
        while not end:
            if current.get_next() is None:
                end = True
            else:
                current = current.get_next()
        current.set_next(temp)
        return True


class NodeTest(unittest.TestCase):
    def setUp(self):
        self.sut: Node = Node(123)

    def test_get_data(self):
        self.assertEqual(self.sut.get_data(), 123)

    def test_get_next(self):
        self.assertEqual(self.sut.get_next(), None)

    def test_set_data(self):
        self.sut.set_data(124)
        self.assertEqual(self.sut.get_data(), 124)

    def test_set_next(self):
        next_node: Node = Node(125)
        self.sut.set_next(next_node)
        self.assertEqual(self.sut.get_next(), next_node)


class UnorderedListTest(unittest.TestCase):
    def setUp(self):
        self.sut: UnorderedList = UnorderedList()

    def test_is_empty(self):
        self.assertEqual(self.sut.is_empty(), True)
        self.sut.add(123)
        self.assertEqual(self.sut.is_empty(), False)

    def test_size(self):
        self.assertEqual(self.sut.size(), 0)
        self.sut.add(123)
        self.assertEqual(self.sut.size(), 1)

    def test_search(self):
        self.assertEqual(self.sut.search(123), False)
        self.sut.add(123)
        self.assertEqual(self.sut.search(123), True)

    def test_remove(self):
        self.sut.add(121)
        self.sut.add(122)
        self.sut.add(123)
        self.sut.add(124)
        self.assertEqual(self.sut.search(123), True)
        self.sut.remove(123)
        self.assertEqual(self.sut.search(123), False)

    def test_get(self):
        base_arr = [124, 123, 122, 121]
        self.sut.add(121)
        self.sut.add(122)
        self.sut.add(123)
        self.sut.add(124)
        self.assertEqual(self.sut.get(), base_arr)

    def test_append(self):
        base_arr = [124, 123, 122, 121, 125, 126]
        self.sut.add(121)
        self.sut.add(122)
        self.sut.add(123)
        self.sut.add(124)
        self.sut.append(125)
        self.sut.append(126)
        self.assertEqual(self.sut.get(), base_arr)
        
if __name__ == '__main__':
    unittest.main()
