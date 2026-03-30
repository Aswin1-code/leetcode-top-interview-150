import random

class RandomizedSet:
    def __init__(self):
        # List to store the elements for O(1) random access
        self.nums = []
        # Dictionary to store the index of each element for O(1) lookup/deletion
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        idx_to_remove = self.val_to_index[val]
        last_val = self.nums[-1]
        self.nums[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
