class Item: # Lista encadeada para armas
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder
        self.next = None
        
    def __str__(self):
        return f"{self.nome} - Poder: {self.poder}" # Retorno com print(item)
    
def encadear_armas(armas):
    prevNode = None
    primeiro_item = None

    for nome, poder in armas:
        item = Item(nome, poder)
        if not primeiro_item:
            primeiro_item = item
        else:
            prevNode.next = item
        prevNode = item

    return primeiro_item
    
espadas = [
    ("Espada Enferrujada", 10),
    ("Lança de Ferro", 15),
    ("Porrete Gigante", 25),
    ("Espada Caça-Dragões", 35)
]

espadaInicial = encadear_armas(espadas)

cajados = [
    ("Cajado de Madeira", 15),
    ("Cajado do Xamã", 30),
    ("Cetro da Luz", 40 ),
    ("Cajado de Fogo", 55)
]

cajadoInicial = encadear_armas(cajados)

arcos = [
    ("Arco Quebrado", 12),
    ("Balestra Improvisada", 20),
    ("Arco Longo da Vila", 30),
    ("Arco do Domador de Dragão", 45)
]

arcoInicial = encadear_armas(arcos)