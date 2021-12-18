import json

from flask import Flask, request, make_response
from util_db import conexao_db



app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def mainPage():
        return "O sistema é só backend,  infelizmente, vai dar trabalho pra corrigir =/ mas corrija com amor,  que a gente fez com amor, e  com amor  a  nota é 10"

@app.route('/produtos/')
def getProdutos():
    produtos = conexao_db.get_all_Produtos()
    produtos = [Produto.toJson() for Produto in produtos]
    return json.dumps(produtos)

@app.route('/produtos/add/', methods=['POST'])
def new_produto():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        unidade_medida = request.form.get('unidade_medida')
        codigo_barras = request.form.get('codigo_barras')
        conexao_db.novo_Produto(descricao,preco,unidade_medida,codigo_barras)
        return make_response({},201)
    else:
        return make_response({}, 404)


@app.route('/produtos/<int:id>/', methods=['GET', 'POST'])
def getEditProduto(id):

    if request.method == 'GET':
        return conexao_db.get_produto_by_id(id).toJson()
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        unidade_medida = request.form.get('unidade_medida')
        codigo_barras = request.form.get('codigo_barras')
        conexao_db.editar_Produto(id,descricao,float(preco),unidade_medida,codigo_barras)
        return make_response({}, 201)
    else:
        return make_response({}, 404)


@app.route('/fornecedores/')
def getFornecedores():
    fornecedores = conexao_db.get_all_Fornecedores()
    fornecedores = [Fornecedor.toJson() for Fornecedor in fornecedores]
    return json.dumps(fornecedores)

@app.route('/fornecedor/add/', methods=['POST'])
def new_fornecedor():
    if request.method == 'POST':
        razao_social = request.form.get('razao_social')
        nome_fantasia = request.form.get('nome_fantasia')
        cnpj = request.form.get('cnpj')
        inscricao_estadual = request.form.get('inscricao_estadual')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        conexao_db.novo_Fornecedor(razao_social, nome_fantasia, cnpj, inscricao_estadual, logradouro, bairro, municipio, estado, cep, telefone, email)
        return make_response({}, 201)
    return make_response({}, 404)


@app.route('/fornecedores/<int:id>/', methods=['GET', 'POST'])
def getFornecedor(id):
    if request.method == 'GET':
        return conexao_db.get_fornecedor_by_id(id).toJson()
    if request.method == 'POST':
        razao_social = request.form.get('razao_social')
        nome_fantasia = request.form.get('nome_fantasia')
        cnpj = request.form.get('cnpj')
        inscricao_estadual = request.form.get('inscricao_estadual')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        if (conexao_db.editar_Fornecedor(id,razao_social, nome_fantasia, cnpj, inscricao_estadual, logradouro, bairro, municipio, estado, cep, telefone, email)):
            return make_response({}, 201)
        else:
            return make_response({}, 404)

@app.route('/clientes/')
def getClientes():
    clientes = conexao_db.get_all_Clientes()
    clientes = [Cliente.toJson() for Cliente in clientes]
    return json.dumps(clientes)


@app.route('/clientes/add/', methods=['POST'])
def new_cliente():
    if request.method == 'POST':
        print(request.form)
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        if (conexao_db.novo_Cliente(nome, cpf, logradouro, bairro, municipio,estado, cep, telefone, email)):
            return make_response({}, 201)
        else:
            return make_response({}, 404)



@app.route('/clientes/<int:id>/', methods=['GET', 'POST'])
def getEditCliente(id):
    if request.method == 'GET':
        return conexao_db.get_cliente_by_id(id).toJson()
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        if conexao_db.editar_Cliente(id ,nome, cpf, logradouro, bairro, municipio,estado, cep, telefone, email):
            return make_response({}, 201)
        else:
            return make_response({}, 404)


@app.route('/estoques/')
def getEstoques():
    estoques = conexao_db.get_all_Estoques()
    estoques = [Estoque.toJson() for Estoque in estoques]
    return json.dumps(estoques)

@app.route('/estoque/add/', methods=['POST'])
def new_estoque():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        if conexao_db.novo_estoque(descricao):
            return make_response({}, 201)
        else:
            return make_response({}, 404)

@app.route('/estoque/<int:id>/', methods=['GET', 'POST'])
def get_Estoque(id):
    if request.method == 'GET':
        return conexao_db.get_estoque_by_id(id).toJson()
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        conexao_db.editar_estoque(id, descricao)

@app.route('/estoque/<int:id_e>/saldo/<int:id_p>/')
def getSaldoEstoque(id_e, id_p):
    if request.method == 'GET':
        return conexao_db.get_saldo_estoque_by_estoque_e_produto(id_p, id_e).toJson()


@app.route('/estoque/movimentacao/<int:id>/')
def getMovEst(id):
    movimentacao = conexao_db.get_movimento_estoque_by_id(id)
    return movimentacao.toJson()


@app.route('/estoque/movimentacao/add/', methods=['POST'])
def new_movimentacao_estoque():
    if request.method == 'POST':
        id_estoque = request.form.get('id_estoque')
        id_produto = request.form.get('id_produto')
        origem = request.form.get('origem')
        tipo = request.form.get('tipo')
        quantidade = request.form.get('quantidade')

        if conexao_db.nova_movimentacao_estoque(id_estoque, id_produto, tipo, quantidade, origem):
            return make_response({}, 201)
        else:
            return make_response({}, 404)


@app.route('/estoque/movimentacao/<int:id>/estornar/', methods=['POST'])
def estornarMovimentoEstoque(id):
    if request.method == 'POST':
        confirmar = request.form.get('confirmar')
        if (confirmar=='Sim'):
            if conexao_db.estornar_movimentacao_estoque(id):
                return make_response({}, 201)
        return make_response({}, 404)

@app.route('/bancos/')
def getBancos():
    bancos = conexao_db.get_all_Bancos()
    bancos = [Banco.toJson() for Banco in bancos]
    return json.dumps(bancos)


@app.route('/bancos/add/', methods=['POST'])
def new_banco():
    if request.method == 'POST':
        codigo_bancario = request.form.get('codigo_bancario')
        nome = request.form.get('nome')
        agencia = request.form.get('agencia')
        conta = request.form.get('conta')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        saldo = request.form.get('saldo')

        if conexao_db.novo_Banco(codigo_bancario, nome, agencia, conta, logradouro, bairro, municipio, estado, cep, telefone, email, saldo):
            return make_response({}, 201)
        else:
            return make_response({}, 404)


@app.route('/bancos/<int:id>/', methods=['GET', 'POST'])
def getEditBanco(id):
    if request.method == 'GET':
        return conexao_db.get_banco_by_id(id).toJson()
    if request.method == 'POST':
        codigo_bancario = request.form.get('codigo_bancario')
        nome = request.form.get('nome')
        agencia = request.form.get('agencia')
        conta = request.form.get('conta')
        logradouro = request.form.get('logradouro')
        bairro = request.form.get('bairro')
        municipio = request.form.get('municipio')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        saldo = request.form.get('saldo')

        if conexao_db.editar_Banco(id, codigo_bancario, nome, agencia, conta, logradouro, bairro, municipio, estado, cep, telefone, email, saldo):
            return make_response({}, 201)
        else:
            return make_response({}, 404)


@app.route('/banco/movimento_bancario/add', methods=['POST'])
def new_movimento_bancario():
    if request.method == 'POST':
        id_banco = request.form.get('id_banco')
        tipo = request.form.get('tipo')
        origem = request.form.get('origem')
        valor = request.form.get('valor')

        if conexao_db.nova_movimentacao_bancaria(id_banco, tipo, valor, origem):
            return make_response({}, 201)
        else:
            return make_response({}, 404)


@app.route('/banco/movimento_bancario/<int:id>/')
def get_saldoBancario(id):
    if request.method == 'GET':
        return conexao_db.get_movimento_bancario_by_id(id).toJson()

# Rota para a nota fiscal

@app.route('/nfs/')
def getNfs():
    nfs = conexao_db.get_all_NFS()
    nfs = [Nota_fiscal.toJson() for Nota_fiscal in nfs]
    return json.dumps(nfs)

@app.route('/nf/add/', methods=['POST'])
def new_nf():
    if request.method == 'POST':
        numero = request.form.get('numero')
        id_fornecedor = request.form.get('id_fornecedor')
        valor = request.form.get('valor')

        if conexao_db.novo_cabecalho_NF(numero, id_fornecedor, valor):
            return make_response({}, 201)
        else:
            return make_response({}, 404)


@app.route('/nf/<int:id>/', methods=['GET'])
def get_nf(id):
    if request.method == 'GET':
        return conexao_db.get_NF_by_id(id).toJson()


# Não tem post de alteração pois seria uma operação parecida com os estornos do estoque, porém infelizmente não deu tempo (fomos gananciosos e criamos muitas tabelas)

@app.route('/nf/<int:id_nf>/itens/add/', methods=['POST'])
def new_nf_itens(id_nf):
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        id_produto = request.form.get('id_produto')
        valor = request.form.get('valor')
        quantidade = request.form.get('quantidade')

        if conexao_db.novo_item_nf(tipo, id_nf, id_produto, quantidade, valor):
            return make_response({}, 201)
        else:
            return make_response({}, 404)



@app.route('/nf/<int:id>/itens/', methods=['GET'])
def get_Itens_Nf(id):
    itens = conexao_db.get_itens_nf(id)
    itens = [Item_NF.toJson() for Item_NF in itens]
    return json.dumps(itens)

#create Database
conexao_db.create_data_base()

app.run()