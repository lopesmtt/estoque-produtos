from produto import Produto
from estoque import Estoque

def menu():
    print("\n=== MENU ESTOQUE ===")
    print("1- Listar produtos")
    print("2- Cadastrar novo produto")
    print("3- Buscar produto por id")
    print("4- Buscar produto por nome")
    print("5- Entrada de produto(aumentar estoque)")
    print("6- Saida de produto(diminuir estoque)")
    print("7- Relatorio de estoque")
    print("8 Salvar e sair")
    print("========================")


def main():
    estoque = Estoque()
    estoque.carregar_de_arquivo()

    def menu():
        print("\n=== MENU ESTOQUE ===")
        print("1 - Listar produtos")
        print("2 - Cadastrar novo produto")
        print("3 - Buscar produto por ID")
        print("4 - Buscar produto por nome")
        print("5 - Entrada de produto (aumentar estoque)")
        print("6 - Saída de produto (diminuir estoque)")
        print("7 - Relatório de estoque baixo")
        print("8 - Salvar e sair")
        print("======================")

def main():
    estoque = Estoque()
    estoque.carregar_de_arquivo()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            estoque.listar_produtos()

        elif opcao == "2":
            try:
                id_produto = int(input("ID: "))
                nome = input("Nome: ")
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço: "))
                estoque.cadastrar_produto(id_produto, nome, quantidade, preco)
                print("Produto cadastrado.")
            except ValueError:
                print("Dados inválidos.")

        elif opcao == "3":
            try:
                id_busca = int(input("Digite o ID do produto: "))
                produto = estoque.buscar_por_id(id_busca)
                print(produto if produto else "Produto não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            nome_busca = input("Digite o nome do produto: ")
            encontrados = estoque.buscar_por_nome(nome_busca)
            if encontrados:
                for p in encontrados:
                    print(p)
            else:
                print("Nenhum produto encontrado.")

        elif opcao == "5":
            try:
                id_produto = int(input("ID do produto para entrada: "))
                quantidade = int(input("Quantidade para adicionar: "))
                produto = estoque.buscar_por_id(id_produto)
                if produto:
                    produto.quantidade += quantidade
                    print("Entrada registrada.")
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("Dados inválidos.")

        elif opcao == "6":
            try:
                id_produto = int(input("ID do produto para saída: "))
                quantidade = int(input("Quantidade para remover: "))
                produto = estoque.buscar_por_id(id_produto)
                if produto:
                    if quantidade > produto.quantidade:
                        print("Quantidade em estoque insuficiente.")
                    else:
                        produto.quantidade -= quantidade
                        print("Saída registrada.")
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("Dados inválidos.")

        elif opcao == "7":
            try:
                limite = int(input("Mostrar produtos com estoque abaixo de: "))
                estoque.relatorio_estoque_baixo(limite)
            except ValueError:
                print("Valor inválido.")

        elif opcao == "8":
            estoque.salvar_em_arquivo()
            print("Estoque salvo. Encerrando programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

        
                                         

   
if __name__=="__main__":
    main()    