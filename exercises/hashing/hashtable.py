import platform
import random

class Node:
    def __init__(self, init_data, value):
        self.data = init_data
        self.value = value
        self.next = None

    def get_data(self):
        return self.data

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_value(self, new_value):
        self.value = new_value


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item, value):
        temp = Node(item, value)
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

        return current.get_value()

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

class Hashtable(object):
    
    n = 0
    m = 1
    table = []
    prime = 2
    sparseness = 4
    w = 64
    words = []
    collisions = 0
    
    def __init__(self, n):
        self.prime = self.get_prime(len(self.table))
        self.n = n
        self.m = self.n * self.sparseness
        self.a = random.randrange(0, self.prime-1)
        self.b = random.randrange(0, self.prime-1)
        self.table = [None] * self.m
        self.w = self.get_w_size()
        self.prepare_words(n)
    
    def prepare_words(self, n):
        wfile = open('/usr/share/dict/words')
        self.words = wfile.read().split()[:n]
    
    def get_w_arch(self):
        word_size = platform.architecture()
        return word_size[0]
        
    
    def get_w_size(self):
        if self.get_w_arch() == '64bit':
            return 64
        return 32 # we dont cater for other archs
        
    
    def get_prime(self, size):
        '''
        We are not aiming at speed here
        so we use Sieve of Eratosthenes from a 2 * size pool and just get the biggest
        '''
        is_prime = [True] * (size + 1)
        div = 2
        while (div * div) <= size:
            if is_prime[div]:
                i = 2 * div
                while i <= size:
                    is_prime[i] = False
                    i += div
            div += 1
                    
        for i in range(len(is_prime)-1, -1, -1):
            if is_prime[i]:
                self.prime = i
                return i
                
                
    def resize_table(self, m, n):
        newtable = [None] * n
        self.table.extend(newtable)
        return self.table
        
    
    def get_hash_division(self, key):
        return key % self.prime
        
    # this is not working atm, but this is the theory
    def get_hash_multiplication(self, key):
        return [(a*key) % 2 ** self.w] >> (self.w - r)
        
    def get_hash_universal(self, key):
        return ((self.a * key + self.b) % self.prime) % len(self.table)
    
        
    def get_alpha(self):
        return str(self.n / (self.m - self.collisions))
    
    def get_hashkey(self, word):
        prehashcode = hash(word)
        return hashtable.get_hash_universal(prehashcode)
        
    
    def add_item(self, item, value):
        key = self.get_hashkey(item)
        if self.table[key] is not None:
            self.collisions += 1
            self.table[key].add(item, value)
        linked_list = UnorderedList()
        linked_list.add(item, value)
        self.table[key] = linked_list
        return key
        
    
    def get_item(self, item):
        key = self.get_hashkey(item)
        if self.table[key] is not None:
            return self.table[key].search(item)
        
    
hashtable = Hashtable(100)
for index, word in enumerate(hashtable.words):
    print('{} encodes to {}'.format(word, hashtable.add_item(word, index)))
    

print('Collisions {}'.format(hashtable.collisions))
print('Load factor is {}'.format(hashtable.get_alpha()))
desired_item = hashtable.words[random.randint(0, 100)]
print('Fetching random word from table -> {}'.format(desired_item))
print('Value for {} is {}'.format(desired_item, hashtable.get_item(desired_item)))