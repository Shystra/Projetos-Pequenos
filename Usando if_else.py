nome = input("Digite o seu nome completo: ")
idade = input("Digite a sua idade: ")
trabalho = input("Você trabalha [Sim/Não]? ")
endereço = input("Local do trabalho: ")
cidade = input("Nome da cidade: ")



if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' or 'Sim' in nome and trabalho and cidade and endereço:
        print("Seu nome contém espaços")
        print("{} é empregado CLT e trabalha no {} em {}".format(trabalho,endereço,cidade))
        
    else:
        print("Seu nome não contem espaços")
        print("{} não é empregado".format(nome))
        

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    
else:
    print("Desculpe, você deixou campos vazios")

    


