class Item_NF():
    def __init__(self, id, tipo,  produto,estoque, quantidade,valor,  dataEntrada):
        self.id = id
        self.tipo = tipo
        self.produto = produto
        self.estoque = estoque
        self.quantidade = quantidade
        self.valor = valor
        self.dataEntrada = dataEntrada

    def toJson(self):
        return dict(
            id=self.id,
            tipo = self.tipo,
            produto= self.produto,
            estoque = self.estoque,
            quantidade = self.quantidade,
            valor = self.valor,
            data_entrada=self.dataEntrada,
        )