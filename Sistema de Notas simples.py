import numpy as np

# Configuração inicial
TOTAL_ALUNOS = 50
# Criamos a lista de nomes e inicializamos as notas com zero usando NumPy
alunos = [f"Aluno_{i}" for i in range(1, TOTAL_ALUNOS + 1)]
notas = np.zeros(TOTAL_ALUNOS)

def exibir_menu():
    print("\n" + "="*30)
    print("      SISTEMA ESCOLAR")
    print("="*30)
    print("1. Ver lista de alunos e notas💯")
    print("2. Alterar nome de um aluno🧑‍🎓")
    print("3. Lançar/Alterar nota de um aluno💯")
    print("4. Ver estatísticas da turma (Média/Maior/Menor)😒")
    print("0. Sair🚪")
    return input("Escolha uma opção: ")

while True:
    opcao = exibir_menu()

    if opcao == "1":
        print("\n--- ⚡ LISTA DE ALUNOS ⚡ ---")
        for i in range(TOTAL_ALUNOS):
            print(f"Índice {i:2} | Nome: {alunos[i]:<15} | Nota: {notas[i]:.1f}")
    
    elif opcao == "2":
        try:
            idx = int(input(f"Digite o índice do aluno (0 a {TOTAL_ALUNOS-1}): "))
            novo_nome = input("Digite o novo nome: ")
            print(f"Alterando {alunos[idx]} para {novo_nome}...")
            alunos[idx] = novo_nome
        except (ValueError, IndexError):
            print("Erro: Índice inválido!")

    elif opcao == "3":
        try:
            idx = int(input(f"Digite o índice do aluno (0 a {TOTAL_ALUNOS-1}): "))
            nova_nota = float(input(f"Digite a nota para {alunos[idx]}: "))
            if 0 <= nova_nota <= 10:
                notas[idx] = nova_nota
                print("Nota atualizada com sucesso!")
            else:
                print("Erro: A nota deve ser entre 0 e 10.")
        except (ValueError, IndexError):
            print("Erro: Entrada inválida!")

    elif opcao == "4":
        print("\n--- ESTATÍSTICAS DA TURMA ---")
        print(f"Média Geral: {notas.mean():.2f}")
        print(f"Maior Nota:  {notas.max():.1f}")
        print(f"Menor Nota:  {notas.min():.1f}")
        print(f"Alunos acima da média (7.0): {np.sum(notas >= 7)}")

    elif opcao == "0":
        print("Saindo do sistema... Até logo🫵🫵!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")