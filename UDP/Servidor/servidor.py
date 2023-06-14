import socket, sys
import time
from threading import Thread

HOST = 'localhost'  
PORT = 20001        
BUFFER_SIZE = 1024  

def main(argv):
    try:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as servidor:
             servidor.bind((HOST, PORT))
             while(True):
                try:
                      informacoes = servidor.recvfrom(1024)
                      with open(informacoes[0],'r') as arquivo:
                        cont = 0
                        inicio = time.time()
                        for linha in arquivo.readlines():
                            servidor.sendto(linha.encode('utf-8'), informacoes[1])
                            cont = cont + 1
                        fim = time.time()
                        servidor.sendto('EOF'.encode('utf-8'), informacoes[1])
                        print("Arquivo enviado:", informacoes[0].decode('utf-8'))
                        tempo = fim - inicio
                        resposta = "\n Tempo gasto no enviado do arquivo: %f \n" % tempo
                        respostaContador = 'Número de linhas no arquivo: %d \n' % cont
                        servidor.sendto(resposta.encode('utf-8'),informacoes[1])
                        servidor.sendto(respostaContador.encode('utf-8'),informacoes[1])
                 
                except Exception as error:
                        print(error)
                        return 

    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)        
        return             

if __name__ == "__main__":   
    main(sys.argv[1:])