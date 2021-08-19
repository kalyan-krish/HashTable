class Hashtable:
    def __init__(self,max):
        self.max = max
        self.arr = [None for i in range(self.max)]
        
    def get_hash(self,key): # getting index from hashfunction
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.max

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None


hash = Hashtable(100)

hash['march 6'] = 12
hash['july 6'] = 34
hash['jan 5'] = 45
del hash['jan 5']
print(hash['jan 5'])

print(hash['july 6'])

print(hash['march 6'])

print(hash.arr)

del hash['jan 5']



