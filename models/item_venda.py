class Item_Venda():
    def __init__(self, id,  produto, estoque ,  quantidade, preco, venda):
        self.id = id
        self.produto = produto
        self.estoque = estoque
        self.quantidade = quantidade
        self.preco = preco
        self.venda = venda

    def toJson(self):
        return dict(
            id=self.id,
            produto = self.produto,
            estoque = self.estoque,
            quantidade=self.quantidade,
            preco=self.preco,
            venda=self.venda
        )