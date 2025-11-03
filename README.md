# MPI em Python

Este repositório contém o código desenvolvido para o **trabalho da disciplina de Sistemas Distribuídos** da **Universidade Federal da Grande Dourados (UFGD)**.  

O objetivo do trabalho é **medir a latência e a largura de banda de comunicação entre dois processos MPI**, utilizando a técnica de *ping-pong*.  

O código envia e recebe arrays de `double` de tamanhos crescentes entre dois processos e calcula:
- O **tempo total** de ida e volta (em segundos)
- A **taxa de transferência** em MB/s
- O **tamanho do vetor** enviado

---

## Conteúdo do repositório

- `pingpong.py` — código principal do experimento em Python usando `mpi4py`
- `README.md` — instruções e explicações sobre o trabalho

---

## Tecnologias utilizadas

- **Python 3.10+**
- **mpi4py** — interface Python para MPI
- **Microsoft MPI (MS-MPI)** — implementação MPI para Windows

---

## Estrutura do código

O código realiza os seguintes passos:

1. Inicializa o MPI e identifica os processos (`rank` e `size`).
2. Verifica se existem exatamente **2 processos** (requisito do trabalho).
3. Para cada tamanho `n = 2^0, 2^1, ..., 2^19`:
   - Gera um vetor de doubles aleatórios.
   - O processo 0 envia o vetor para o processo 1.
   - O processo 1 recebe o vetor e envia de volta ao processo 0 (*ping-pong*).
   - Mede o **tempo de ida e volta** e calcula a **taxa de transferência**.
   - Imprime uma tabela com: tipo, tamanho, tempo e taxa.

---

## Como executar

### 1. Instalar dependências

**Python 3.10+** e `mpi4py`:

```bash
pip install mpi4py
````
**Microsoft MPI (Windows)**

  - Baixe e instale MS-MPI v10.1.3:
  -- Runtime: msmpisetup.exe
  -- SDK (opcional, se desejar compilar em C): msmpisdk.msi
  -- No Windows, o comando de execução é mpiexec (não mpirun).

### 2. Rodar o código
Execute no terminal / PowerShell:
```bash
mpiexec -n 2 python script.py
````
⚠️ É obrigatório usar 2 processos (-n 2).

## Observações

- Esse código serve para **avaliar desempenho de comunicação ponto-a-ponto** entre dois processos MPI em um cluster ou em uma máquina local.
- Os valores de tempo e taxa dependem do computador, da rede e da configuração do sistema utilizados.
- É **importante executar com exatamente dois processos** (`-n 2`), caso contrário o código encerra com a mensagem de aviso.
- Para relatórios acadêmicos, é possível **salvar os resultados em CSV** ou gerar gráficos de desempenho para análise visual.

---

## Autor

**Pedro Barbosa**  
Bacharelado em Sistemas de Informação  
Universidade Federal da Grande Dourados (UFGD)
