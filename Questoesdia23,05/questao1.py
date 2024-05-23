alunos = {1:1.6, 2:1.8, 3:1.78, 4:1.66, 5:1.57, 6:1.70}
for n_aluno, altura in alunos.items():
    if altura >= 1.8:
        print(f'a altura do aluno {n_aluno} é {altura}, ele possui a maior altura')
    elif altura <= 1.57:
        print(f'a altura do aluno {n_aluno} é {altura}, ele possui a menor altura.')