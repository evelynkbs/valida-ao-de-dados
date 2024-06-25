class Cadastro:
    nome = None
    idade = None
    saldo = None
    statusCadastro = None
    endereco = None

    def __init__(self):
        print("construtor")

    def InserirNome(self, nome):
        Correta = self.ValidaNome(nome)
        if Correta == True:
            self.nome = nome
            print("Nome cadastrado com sucesso")

    def ValidaNome(self, nome):
        if len(nome) == 0:
            print("O valor nome não pode ser vazio")
            return False
        else:
            return True


   

    def InserirIdade(self, idade):
        Correta = self.ValidaIdade(idade)
        if Correta == True:
            self.idade = idade
            print("Idade cadastrado com sucesso")

    def ValidaIdade(self, idade):
        if idade <= 0:
            print("Idade precisa ser positiva")
            return False
        else:
            return True
       


    def InserirSaldo(self, saldo):
        saldoCorreto = self.ValidaSaldo(saldo)
        if saldoCorreto == True:
            self.idade = saldo
            print("Saldo cadastrado com sucesso")

    def ValidaSaldo(self, saldo):
        if saldo <= 0:
            print("Saldo precisa ser positiva")
            return False
        else:
         return True
       

    def InserirStatusCadastro(self, StatusCadastro):
        Correto = self.ValidaStatusCadastro(StatusCadastro)
        if Correto == True:
            self.StatusCadastro = StatusCadastro
            print("Status do cadastro cadastrado com sucesso")

    def ValidaStatusCadastro(self, StatusCadastro):
        if StatusCadastro <= 0:
            print("Status do cadastro não pode ser vazio")
            return False
        else:
           return True


    def InserirEndereco(self, Endereco):
        Correto = self.ValidaEndereco(Endereco)
        if Correto == True:
            self.Endereco = Endereco
            print("Endereço cadastrado com sucesso")

    def ValidaEndereco(self, Endereco):
        if len(Endereco) >= 3:
            return True
        else:
            print("Endereço não pode ser vazio")
            return False
           


cadastro1 = Cadastro()
cadastro1.InserirNome("Ana")
cadastro1.InserirIdade(20)
cadastro1.InserirSaldo(5000)
cadastro1.InserirStatusCadastro(True)
cadastro1.InserirEndereco("Rua São Paulo")
