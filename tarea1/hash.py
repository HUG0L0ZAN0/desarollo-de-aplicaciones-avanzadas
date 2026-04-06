class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return
        raise KeyError(f"Key '{key}' not found")

    def contains(self, key):
        index = self._hash(key)
        return any(pair[0] == key for pair in self.table[index])

    def keys(self):
        result = []
        for bucket in self.table:
            for pair in bucket:
                result.append(pair[0])
        return result

    def values(self):
        result = []
        for bucket in self.table:
            for pair in bucket:
                result.append(pair[1])
        return result


ht = HashTable()

print("esta vacio?", ht.keys() == [])

ht.insert("nombre", "Hugo")
ht.insert("edad", 22)
ht.insert("carrera", "ITC")

print("keys:", ht.keys())
print("values:", ht.values())

print("get nombre:", ht.get("nombre"))
print("contiene 'edad'?", ht.contains("edad"))

ht.insert("nombre", "Hugo Lozano")
print("update nombre:", ht.get("nombre"))

ht.delete("edad")
print("keys despues de delete:", ht.keys())

try:
    ht.get("edad")
except KeyError as e:
    print("KeyError:", e)