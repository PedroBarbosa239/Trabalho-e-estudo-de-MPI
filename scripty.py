
#    Problema:
#       Escreva um programa para medir o tempo que leva para enviar/receber 20, 21, 22, . . ., 219 valores
#    do tipo double de um processador para outro usando MPI_Send e MPI_Recv. Os valores devem ser
#    gerados aleatoriamente e vocˆe deve considerar que o mesmo dado deve ser enviado e recebido por uma
#    mesma m ́aquina (ping pong). Ou seja, a m ́aquina P0 deve enviar e receber um valor e somente depois
#    ela poder ́a enviar e receber o pr ́oximo valor da sequˆencia. O mesmo deve ser valido para P1.
#    Como saıda, seu programa deve imprimir o tamanho, o tempo e a taxa em MB/s para cada teste.
#    Para a taxa, uma sugest ̃ao  ́e pensar no tamanho do dado enviado e no tempo para enviar 1  ́unico dado.
#    A sa ıda do programa deve ser algo como na tabela a seguir, onde n n ̃ao  ́e o valor, mas o tamanho do
#    dado enviado, isto  ́e, um array de tamanho n:
#   
#   Requisitos:
#    -- Python 3.12
#    -- pip install mpi4py
#    -- mpi microsoft (realizar download)
#


from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if size != 2:
    if rank == 0:
        print("Precisa de exatamente 2 processos MPI.")
    MPI.Finalize()
    exit()

if rank == 0:
    print(f"{'Tipo':<10}{'n':>10}{'Tamanho (MB)':>15}{'Tempo (s)':>15}{'Taxa (MB/s)':>15}")

for i in range(20):
    n = 2 ** i
    data = np.random.random(n).astype('d')  
    comm.Barrier()  
    start = MPI.Wtime()  

    if rank == 0:
        comm.Send([data, MPI.DOUBLE], dest=1, tag=0)
        comm.Recv([data, MPI.DOUBLE], source=1, tag=0)
    elif rank == 1:
        comm.Recv([data, MPI.DOUBLE], source=0, tag=0)
        comm.Send([data, MPI.DOUBLE], dest=0, tag=0)

    end = MPI.Wtime()  
    sub = end - start

    bytes_transmitidos = 2 * n * data.itemsize 
    tamanho_mb = (n * data.itemsize) / (1024 * 1024)
    taxa = (bytes_transmitidos / (1024 * 1024)) / sub

    if rank == 0:
        print(f"{'Send/Recv':<10}{n:>10}{tamanho_mb:>15.6f}{sub:>15.6f}{taxa:>15.3f}")
