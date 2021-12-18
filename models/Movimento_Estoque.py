class Movimento_Estoque():
    def __init__(self, id, origem, tipo, produto, estoque,  quantidade, dataMovimento):
        self.id = id
        self.origem = origem
        self.tipo = tipo
        self.produto = produto
        self.estoque = estoque
        self.quantidade = quantidade
        self.dataMovimento = dataMovimento

    def toJson(self):
        return dict(
            id=self.id,
            origem = self.origem,
            tipo = self.tipo,
            produto = self.produto,
            estoque = self.estoque,
            quantidade = self.quantidade,
            dataMovimento = self.dataMovimento
        )