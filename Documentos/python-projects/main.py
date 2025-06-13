alunos = []
def menu ():
    print("\n=== Menu ===")
    print("1. Cadastrar aluno")
    print("2. Exibir alunos")
    print("3. Buscar aluno por nome")
    print("4. Filtrar por média")
    print("5. Sair")

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    notas = []

    for i in range(3):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas) 
    status = "Aprovado" if media >= 7 else "Reprovado"

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "status": status
    }   

    alunos.append(aluno)
    print(f"Aluno '{nome}' cadastrado com sucesso! ")

def exibir_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
        return
    
    print("\n=== Lista de Alunos ===")
    for aluno in alunos:
        print(f"Nome: {aluno ['nome']}")
        print(f"Notas: {aluno ['notas']}")
        print(f"Media: {aluno['media']: .2f}")
        print(f"Status: {aluno['status']}")
        print("-"* 30)

    
def buscar_aluno():
    nome_busca = input("Digite o nome do aluno para buscar: ")

    encontrado = False
    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            print(f"\nAluno encontrado: ")
            print(f"Nome: {aluno['nome']}")
            print(f"Notas: {aluno['notas']}")
            print(f"Media: {aluno['media']:.2f}")
            print(f"Status: {aluno['status']}")
            print("-" * 30)
            encontrado = True
            break
        if not encontrado:
            print(f"Nenhum aluno chamado '{nome_busca}' foi encontrado ")    

def filtrar_por_media():
    try:
        media_min = float(input("Digite a media minima: "))
    except ValueError:
        print("Entrada invalida. Digite um numero valido.")
        return
    
    encontrados = False
    print(f"\nAlunos com media >= {media_min}:")
    for aluno in alunos:
        if aluno["media"] >= media_min:
            print(f"Nome: {aluno['nome']}")
            print(f"Media: {aluno['media']:.2f}")
            print(f"Status: {aluno['status']}")
            print("-" * 30)
            encontrados = True
    if not encontrados:
             print("Nenhum aluno encontrado com essa media minima.")   

while True:
    menu()
    opcao = input("Escolha uma opçao: ")


    if opcao == "1":
        cadastrar_aluno() 
    elif opcao == "2":
        exibir_alunos()
    elif opcao == "3":
        buscar_aluno()
    elif opcao == "4":
        filtrar_por_media()
    elif opcao == "5":
        print("Saindo...")
    else:
        print("Opçao invalida")    


