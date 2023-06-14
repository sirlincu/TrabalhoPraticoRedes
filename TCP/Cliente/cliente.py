import socket, sys
   
host ='localhost'
porta = 7777

def menu():
    print('\n')
    print("--------------Menu de opcoes------------------")
    print('1- Arquivo Pequeno')
    print('2- Arquivo medio')
    print('3- Arquivo grande')

def  getArquivo (opcao):
    if opcao == 1:
        nomeDoArquivo = 'small.txt'
        return nomeDoArquivo
    elif opcao == 2:
        nomeDoArquivo = 'medium.txt'
        return nomeDoArquivo 
    elif opcao == 3:
        nomeDoArquivo = 'large.txt'
        return nomeDoArquivo


def main(argv,arquivo):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as cliente:
                cliente.connect((host,porta))
                cliente.send(arquivo.encode('utf-8'))
                with open(arquivo, 'w') as file:
                    while True:
                            data = cliente.recv(102400).decode('utf-8')
                            if data == "EOF":
                                print('Arquivo recebido: ', arquivo)
                                tempo = cliente.recv(1024).decode('utf-8')
                                print(tempo)
                                contador = cliente.recv(1024).decode('utf-8')
                                print(contador)
                                break
                            else:                            
                                file.write(data)
    except Exception as error:
        print(error)
        print('Execao - Programa sera encerrado Lado cliente')
        return


if __name__ == "__main__":
    opcao = 0
    menu()
    opcao = int(input('Qual sua escolha: '))
    arquivo = getArquivo(opcao)
    main(sys.argv[1:],arquivo) 
    
    while True:
            print('1- Deseja enviar outro Arquivo')
            print('2- Encerrar a aplicação')
            escolha = int(input('Qual sua escolha: '))
            if escolha == 2:
                break
            elif escolha < 1 or escolha > 2:
                 print('opcao invalida')
                 print('tente novamente')
            else:
                 menu()
                 x = int(input('Qual sua escolha: '))
                 arquivo = getArquivo(x)
                 main(sys.argv[1:],arquivo) 
   