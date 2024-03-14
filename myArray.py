class MyArray:
    def __init__(self) -> None:
        self.list = []

    def add(self, obj):
        self.list.append(obj) 
    
    def size(self) -> int:
        return len(self.list)
    
    def get(self, pos) -> int:
        return self.list[pos]