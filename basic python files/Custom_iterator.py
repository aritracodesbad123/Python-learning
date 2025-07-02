class CountDown:
    def __init__(self,Timer):
        self.Timer = Timer
        self.counter = 1
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter <= self.Timer:
            value = self.Timer
            self.Timer-=1
            return value
        else:
            raise StopIteration
        
cd = CountDown(10)

for num in cd:
    print(num)