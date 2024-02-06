"""
DATA.             17/05/2023
PROGRAM-ID.       PROG.31
AUTOR/DEV.        Carlos Henrique e Daniel Teodoro
DESCRIÇÃO.        LISTA ALUNOS
"""
# Média de Notas e Status de Aprovação
alunos = []

# Solicitar o número de alunos
quantidade_alunos = int(input("Digite o número de alunos(as): "))

# Solicitar o nome e a data de cada aluno
for i in range(quantidade_alunos):
  nome = input(f"Digite o nome do aluno {i+1}: ")
  nota = float(input(f"Digite a nota do aluno {nome}:"))
  alunos.append((nome, nota))

# Verificar e imprimir o status de aprovação de cada aluno
for aluno in alunos:
  nome = aluno[0]
  nota = aluno[1]
  if nota >= 6:
    print(f"{nome} está Aprovado")
  else:
    print(f"{nome} está Reprovado")