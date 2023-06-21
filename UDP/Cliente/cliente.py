import socket, sys

HOST = 'localhost' 
PORT = 7777       
BUFFER_SIZE = 9999999 

def menu():
    print('\n')
    print("--------------Menu de opções------------------")
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
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as cliente:
            cliente.sendto(arquivo.encode(), (HOST, PORT))
            with open(arquivo, 'w') as file:
                    while True:
                            data = cliente.recvfrom(BUFFER_SIZE)
                            linha = "{}".format(data[0].decode('utf-8'))

                            if linha == 'EOF':

                                print('Arquivo recebido:', arquivo)

                                tempo = cliente.recvfrom(BUFFER_SIZE)
                                print(tempo[0].decode('utf-8'))
                              
                                contador = cliente.recvfrom(BUFFER_SIZE)
                                print(contador[0].decode('utf-8'))
                                break
                            else:                            
                                file.write(linha)
         
    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return
    
if __name__ == "__main__":
    opcao = 0
    menu()
    opcao = int(input('Qual sua escolha: '))
    arquivo = getArquivo(opcao)
    main(sys.argv[1:],arquivo) 
    
    while True:
            print('\n')
            print('1- Deseja enviar outro Arquivo')
            print('2- Encerrar a aplicação')
            escolha = int(input('Qual sua escolha: '))
            if escolha == 2:
                break
            elif escolha < 1 or escolha > 2:
                 print('Opção Inválida!')
                 print('Tente novamente...')
            else:
                 menu()
                 x = int(input('Qual sua escolha: '))
                 arquivo = getArquivo(x)
                 main(sys.argv[1:],arquivo) 
   