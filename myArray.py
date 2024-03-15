class MyArray:
    def __init__(self) -> None:
        self.list = []

    def add(self, obj):
        self.list.append(obj) 
    
    def size(self) -> int:
        return len(self.list)
    
    def get(self, pos) -> int:
        return self.list[pos]
    
    # Ordena pelo nome do atributo da lista usando essa lambda que está abaixo.
    def sort(self, nomeAtributo) -> None:
        self.list.sort(key=lambda number: number[nomeAtributo])