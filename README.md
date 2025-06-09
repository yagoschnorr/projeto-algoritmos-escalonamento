# Projeto de algoritmos de escalonamento

Este projeto tem como principal objetivo desenvolver um minijogo que simula uma corrida de processos a partir de políticas de escalonamento para a matéria de Sistemas Operacionais.

## Algoritmos utilizados: 

 - FIFO (First In First Out): O algoritmo de escalonamento FIFO é um algoritmo de baixa complexidade que, em resumo, é uma fila onde o primeiro processo que entra na linha de execução é também o primeiro a sair, quando termina sua execução ou quando ocorre alguma chamada no sistema para que a execução seja interrompida. Um dos problemas relacionados ao algoritmo FIFO é o de que as vezes um processo menor pode ter que esperar muito tempo até poder ser executado, tendo que esperar os processos que entraram na linha de execução antes dele, ocasionando em um tempo de espera médio elevado.
  - Prioridade: O algoritmo de escalonamento por prioridade é um algoritmo onde um número inteiro é associado a cada processo e quanto menor esse número, maior será a prioridade do processo, ou seja, a CPU é alocada ao processo que possui maior prioridade (menor inteiro = maior prioridade). Um dos problemas relacionados ao algoritmo de escalonamento por prioridade é a Estagnação (starvation), onde um processo pode nunca ser executado por conta de sua prioridade ser muito baixa (a solução criada para isso foi chamada de aging ou envelhecimento, que consiste em quanto maior tempo o processo passar esperando mais alta vai ficando a sua prioridade).

## Como executar o jogo:

1. Instale as dependências utilizando o comando:

```
pip install -r requirements.txt
```

2. Em sequência rode o streamlit a partir do comando:

```
streamlit run main.py
```

## Referências:
 - https://www.youtube.com/watch?v=yihJOQrMgls
 - https://www.youtube.com/watch?v=8EckoXGfEV4
 - https://docs.streamlit.io/develop/api-reference
