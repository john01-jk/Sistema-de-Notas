import numpy as np

# --- CONFIGURAÇÃO GLOBAL ---
TOTAL_ALUNOS = 50

# --- Comandos do Menu
def menu():
    print("\n" + "="*40)
    print("       SISTEMA DE NOTAS")
    print("="*40)
    print("1. Ver lista de alunos")
    print("2. Lançar/Alterar nota")
    print("3. Alterar nome de aluno")
    print("4. Estatísticas (Mín/Máx/Média)")
    print("5. Buscar aluno por nome")
    print("6. REMOVER aluno")
    print("7. Ver Sucessor e Antecessor")
    print("0. Sair")
    return input("\nEscolha uma opção: ")

def executar():
    # Inicializa os dados
    alunos, notas = inicializar()

    while True:
        opcao = menu()

        if opcao == "1":
            exibir_lista(alunos, notas)
        
        elif opcao == "2":
            try:
                idx = int(input("Índice do aluno: "))
                nota = float(input(f"Nota para {alunos[idx]}: "))
                if 0 <= nota <= 10:
                    notas[idx] = nota
                    print("Nota atualizada!")
                else:
                    print("Nota deve ser entre 0 e 10.")
            except: print("Erro na entrada.")

        elif opcao == "3":
            try:
                idx = int(input("Índice do aluno: "))
                alunos[idx] = input("Novo nome: ")
                print("Nome alterado!")
            except: print("Erro no índice.")

        elif opcao == "4":
            ver_estatisticas(notas)

        elif opcao == "5":
            buscar_aluno(alunos, notas)

        elif opcao == "6":
            remover_com_shift(alunos, notas)

        elif opcao == "7":
            ver_vizinhos(alunos, notas)

        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    executar()

 # definindo o tamanho do nome que sera colocado nas notas 
def inicializar():
    """
    Cria os arrays de nomes e notas. 
    Usamos 'U20' para permitir nomes com até 20 caracteres.
    """
    nomes = np.array([f"Aluno_{i}" for i in range(1, TOTAL_ALUNOS + 1)], dtype='U20')
    notas = np.zeros(TOTAL_ALUNOS)
    return nomes, notas

def exibir_lista(nomes, notas):
    print("\n" + "-"*40)
    print(f"{'ÍNDICE':<8} | {'NOME':<15} | {'NOTA':<5}")
    print("-"*40)
    for i in range(TOTAL_ALUNOS):
        # Destaca se o campo estiver vazio
        status_nome = nomes[i]
        print(f"[{i:2}]     | {status_nome:<15} | {notas[i]:.1f}")
      

def remover_com_shift(nomes, notas):
    """
    Remove um aluno e desloca todos os sucessores para a esquerda.
    O último elemento do array torna-se 'Vazio'.
    """
    try:
        idx = int(input(f"\nDigite o índice para REMOVER (0 a {TOTAL_ALUNOS-1}): "))
        
        if 0 <= idx < TOTAL_ALUNOS:
            print(f" Removendo {nomes[idx]} e deslocando sucessores...")

            # Algoritmo de Shift com NumPy:
            # 1. Deleta o item (o array diminui para 49 posições temporariamente)
            nomes_temp = np.delete(nomes, idx)
            notas_temp = np.delete(notas, idx)

            # 2. Adiciona o valor vazio ao final (volta para 50 posições)
            # O uso de [:] garante que alteramos o array original na memória
            nomes[:] = np.append(nomes_temp, "Vazio")
            notas[:] = np.append(notas_temp, 0.0)

            print(" Operação concluída: O buraco foi fechado e o final da lista restabelecido.")
        else:
            print(" Erro: Índice fora do intervalo!")
    except ValueError:
        print(" Erro: Entrada inválida. Digite um número.")

def buscar_aluno(nomes, notas):
    termo = input("Digite o nome ou parte dele para buscar: ").lower()
    # np.char.find retorna o índice onde a string começa, ou -1 se não achar
    indices = np.where(np.char.find(np.char.lower(nomes), termo) != -1)[0]
    
    if len(indices) > 0:
        for i in indices:
            print(f" Achado no [Índice {i}]: {nomes[i]} | Nota: {notas[i]}")
    else:
        print("Empty: Nenhum aluno encontrado.")

def ver_estatisticas(notas):
    print("\n--- ESTATÍSTICAS DA TURMA ---")
    print(f"Menor Nota (Mínimo): {notas.min():.1f}")
    print(f"Maior Nota (Máximo): {notas.max():.1f}")
    print(f"Média Geral:         {notas.mean():.2f}")

def ver_vizinhos(nomes, notas):
    try:
        idx = int(input("Ver vizinhos de qual índice? "))
        if 0 <= idx < TOTAL_ALUNOS:
            # Lógica de Predecessor e Sucessor
            pred = nomes[idx-1] if idx > 0 else "--- (Início da Lista)"
            suce = nomes[idx+1] if idx < TOTAL_ALUNOS - 1 else "--- (Fim da Lista)"
            
            print(f"\n Predecessor: {pred}")
            print(f"Aluno Atual: {nomes[idx]} (Nota: {notas[idx]})")
            print(f"Sucessor:    {suce}")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

