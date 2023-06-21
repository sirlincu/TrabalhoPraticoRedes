import socket, sys
import time
from threading import Thread

host ='localhost'
porta = 7777
buffer_size = 9999999

def on_new_client(conexao, endereco):
        while(True):
            try:
                nomeDoArquivo = conexao.recv(buffer_size).decode('utf-8')
                with open(nomeDoArquivo,'r') as arquivo:
                        cont = 0
                        inicio = time.time()
                        for linha in arquivo.readlines():
                            conexao.send(linha.encode('utf-8'))
                            if(cont % 50 == 0):
                                time.sleep(0.0001)
                            cont = cont + 1
                        fim = time.time()
                        conexao.send('EOF'.encode('utf-8'))
                        print("Arquivo enviado:",nomeDoArquivo)
                        tempo = fim - inicio
                        resposta = "\nTempo gasto no envio do arquivo: %f \n" % tempo
                        respostaContador = 'Número de linhas no arquivo: %d \n' % cont
                        conexao.send(resposta.encode('utf-8'))
                        conexao.send(respostaContador.encode('utf-8'))
            except Exception as error:
                        return 
                

def main(args):
        try:
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as servidor:
                servidor.bind((host,porta))
                while True:
                    servidor.listen()
                    connection, address = servidor.accept()
                    print('Conectado ao cliente no endereço: ',address)
                    t = Thread(target=on_new_client, args=(connection,address))
                    t.start()
        except Exception as error:
            print("Exceção - Programa será encerrado! Lado servidor" )
            print(error)
            return

if __name__ == "__main__":
    main(sys.argv[1:])
    