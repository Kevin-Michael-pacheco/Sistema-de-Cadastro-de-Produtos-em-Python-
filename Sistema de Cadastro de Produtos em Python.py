produtos=[]
preco=[]
quantidade=[]
def menu():
    print('======== Menu =========')
    print('1-cadastrar produtos')
    print('2-cadastrar valor dos produtos')
    print('3-cadastrar quantidade dos produtos')
    print('4-ver produtos cadastrados')
    print('5-sair')
    op=int(input("digite a opção que vc deseja realizar : "))
    if op==1:
        qtd_produtos=int(input('digite quantos produtos vai cadastrar : '))
        for i in range(0,qtd_produtos):
            nome=str(input(f'digite o nome do [{i+1}] produto: '))
            produtos.append(nome)
            
        continuar=int(input('se quiser continuar digite 1 ( senão digite 0) : '))
        if continuar==1:
            m=menu()
        else:
            print()
            print('programa encerrado')
    if op ==2:
        cont=len(produtos)
        for i in range(cont):
            valor=float(input(f'digite o valor para o  {produtos[i]} :'))
            preco.append(valor)
        continuar=int(input('se quiser continuar digite 1 (senão digite 0) :'))
        if continuar == 1:
            m=menu()
        else:
            print()
            print('programa encerrado')
    if op ==3:
        cont=len(produtos)
        for i in range(cont):
            qutd=int(input(f'digite quantos {produtos[i]} tem no estoque :'))
            quantidade.append(qutd)
        continuar=int(input('se quiser continuar digite 1 (senão digite 0) :'))
        if continuar ==1:
            m=menu()
        else:
            print()
            print('programa encerrado')
    if op ==4 :      
        cont=len(produtos)
        print('os produtos cadastrados são:')
        for i in range(cont):
            print(f'produto: {produtos[i]} | preco: {preco[i]} | quantidade no estoque: {quantidade[i]}')
        continuar=int(input('se quiser continuar digite 1 (senão digite 0) :'))
        if continuar == 1:
            m=menu()
        else:
            print()
            print('programa encerrado')
    if op == 5:
        print('programa encerrado')
    if op==0 or op<0:
        print()
        print('opção invalida')
        print()
        print('programa encerrado')
            
m=menu()


     
     
