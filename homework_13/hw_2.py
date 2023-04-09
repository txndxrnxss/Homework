class MySquareIterator:
    def __init__(self, iterable) -> None:
        self.iter = iterable
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            result = self.iter[self.index]
        except Exception as err:
            raise StopIteration
        else:
            self.index += 1
            return result**2
        
lst = 
