import platform
import random



class Hashtable(object):
    
    table = []
    prime = 2
    sparseness = 5
    w = 64
    words = []
    
    def __init__(self, n):
        self.table = [None] * (n * self.sparseness)
        self.prime = self.get_prime(len(self.table))
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
        a = random.randrange(0, self.prime-1)
        b = random.randrange(0, self.prime-1)
        return ((a * key + b) % self.prime) % len(self.table)
        
    
    def add_item(self, item, key):
        if self.table[key] is not None:
            return False # how to deal with collisions
        self.table[key] = item
        return self.table
        
    
hashtable = Hashtable(100)
for word in hashtable.words:
    prehashcode = hash(word)
    hashposition = hashtable.get_hash_universal(prehashcode)
    print('Position {}'.format(hashposition))
    hashtable.add_item(word, hashposition)
    
print(hashtable)

        
