class EvenIterator:
    def __init__(self,nums):
        self.nums = nums
        self.counter = 0
        pass
    def __iter__(self):
        return self
    def __next__(self):
        while self.counter < len(self.nums):
            current = self.nums[self.counter]
            self.counter+=1
            if current %2 ==0:
                return current
        raise StopIteration

cd = EvenIterator([2,3,4,5,6,7,8,9,10,11,12])

for nums in cd:
    print(nums)
        
            