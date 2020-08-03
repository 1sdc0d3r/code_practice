'''
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

- add(value): Insert a value into the HashSet.
- contains(value) : Return whether the value exists in the HashSet or not.
- remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
'''


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = dict()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.table:
            self.table[key] = True
            return None

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.table:
            self.table.pop(key)
            return None

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.table:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
print(obj.add("key"))
print(obj.remove("key"))
print(obj.contains("key"))
