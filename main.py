import time
import random
import streamlit as st

def main():
    st.sidebar.title('Barra de navegação')
    escolha = st.sidebar.radio(' ', options=['Início', 'Corrida de algoritmos'], label_visibility='collapsed')

    if escolha == 'Início':
        inicio()
    elif escolha == 'Corrida de algoritmos':
        corrida_algoritmos()

def inicio():
    st.write('## -> Projeto de algoritmos de escalonamento')

    st.divider()

    st.write('''Este projeto tem como principal objetivo desenvolver um minijogo que simula uma corrida de processos a partir de políticas 
             de escalonamento para a matéria de Sistemas Operacionais.''')
    
    st.divider()

    st.write('''
            - #### Algoritmos utilizados: 
                - FIFO (First In First Out): O algoritmo de escalonamento FIFO é um algoritmo de baixa complexidade que, em resumo, é uma fila 
                  onde o primeiro processo que entra na linha de execução é também o primeiro a sair, quando termina sua execução ou quando ocorre 
                  alguma chamada no sistema para que a execução seja interrompida. Um dos problemas relacionados ao algoritmo FIFO é o de que as 
                  vezes um processo menor pode ter que esperar muito tempo até poder ser executado, tendo que esperar os processos que entraram na 
                  linha de execução antes dele, ocasionando em um tempo de espera médio elevado.
                - Prioridade: O algoritmo de escalonamento por prioridade é um algoritmo onde um número inteiro é associado a cada processo e quanto 
                  menor esse número, maior será a prioridade do processo, ou seja, a CPU é alocada ao processo que possui maior prioridade (menor 
                  inteiro = maior prioridade). Um dos problemas relacionados ao algoritmo de escalonamento por prioridade é a Estagnação (starvation), 
                  onde um processo pode nunca ser executado por conta de sua prioridade ser muito baixa (a solução criada para isso foi chamada de 
                  aging ou envelhecimento, que consiste em quanto maior tempo o processo passar esperando mais alta vai ficando a sua prioridade).
    ''')

    st.divider()

    st.write('''
            #### Referências:
            - https://www.youtube.com/watch?v=yihJOQrMgls
            - https://www.youtube.com/watch?v=8EckoXGfEV4
            - https://docs.streamlit.io/develop/api-reference
    ''')

def corrida_algoritmos():
    nome_processos = ['Max Verstappen', 'Fernando Alonso', 'Lewis Hamilton', 'Charles Leclerc', 'Lando Norris', 'Carlos Sainz',
                       'George Russell', 'Sergio Pérez', 'Valtteri Bottas', 'Pierre Gasly', 'Esteban Ocon', 'Oscar Piastri', 
                       'Alexander Albon', 'Nico Hülkenberg', 'Yuki Tsunoda', 'Daniel Ricciardo', 'Lance Stroll', 'Kevin Magnussen', 
                       'Guanyu Zhou', 'Logan Sargeant']

    processos = [[nome_processos[random.randint(0, len(nome_processos)-1)], random.randint(1,10), random.randint(0,10)],
                 [nome_processos[random.randint(0, len(nome_processos)-1)], random.randint(1,10), random.randint(0,10)],
                 [nome_processos[random.randint(0, len(nome_processos)-1)], random.randint(1,10), random.randint(0,10)]]

    st.write('## Corrida de algoritmos de escalonamento 🏁')

    st.divider()

    st.write('##### Selecione o algoritmo que você deseja realizar a corrida abaixo')

    algoritmo = st.selectbox(' ', options=[' ', 'FIFO', 'Prioridade'], label_visibility='collapsed')

    st.divider()

    st.write(f'#### Os processos que estão participando da corrida são:')

    for processo in processos:
        st.write(f'- Nome do processo: {processo[0]}, Tamanho: {processo[1]}, Prioridade: {processo[2]}')

    st.divider()

    if algoritmo == 'FIFO':
        st.write(f'#### Iniciando corrida com o algoritmo FIFO')
        escalonamento_fifo(processos)
    elif algoritmo == 'Prioridade':
        st.write(f'#### Iniciando corrida com o algoritmo de Prioridade')
        escalonamento_prioridade(processos)

def escalonamento_fifo(processos):
    barras = []
    for processo in processos:
        barras.append([processo[0], ['🟥' for _ in range(processo[1])]])

    limpar_tela = st.empty()
    ganhador = ''

    for i, (processo, tempo_cpu, prioridade) in enumerate(processos):
        for j in range(tempo_cpu):
            barras[i][1][j] = '🟩'
            time.sleep(0.5)

            corrida = '' 
            for barra in barras:
                corrida += f'Processo {barra[0]} -> {barra[1]} \n\n'
                if ('🟥' not in barra[1]) & (ganhador == ''):
                    ganhador = barra[0]
                
            limpar_tela.write(corrida)

    st.success(f'##### O vencedor  da corrida foi o processo {ganhador} 🏆🏆🏆')

def escalonamento_prioridade(processos):
    for i in range(len(processos)-1):
        min_indice = i
        for j in range(i+1, len(processos)):
            if processos[j][2] < processos[min_indice][2]:
                min_indice = j
        aux = processos[i]
        processos[i] = processos[min_indice]
        processos[min_indice] = aux

    barras = []
    for processo in processos:
        barras.append([processo[0], ['🟥' for _ in range(processo[1])], processo[2]])

    limpar_tela = st.empty()
    ganhador = ''

    for i, (processo, tempo_cpu, prioridade) in enumerate(processos):
        for j in range(tempo_cpu):
            barras[i][1][j] = '🟩'
            time.sleep(0.5)

            corrida = '' 
            for barra in barras:
                corrida += f'Processo {barra[0]}, Prioridade: {barra[2]} -> {barra[1]}\n\n'
                if ('🟥' not in barra[1]) & (ganhador == ''):
                    ganhador = barra[0]
                
            limpar_tela.write(corrida)

    st.success(f'##### O vencedor da corrida foi o processo {ganhador} 🏆🏆🏆')

if __name__ == '__main__':
    main()