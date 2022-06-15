from datetime import date
from time import sleep
from rich import print
import time
from rich.progress import Progress

class Funcoes:
    def __init__(self): #Iniciando o metodos que vao ser usados
        self.__cand1 = ['LEANDRO VIERSBERG - PDSC, nº 78']  # cand = Candidatos que o usuario quer colocar
        self.__cand2 = ['FLÁVIO SANTOS - PDB, nº 55']
        self.__cand3 = ['RODRIGO SOUZA - PDC, nº 62']
        self.__candCont1 = 0 # candCont = Contagem de votos para cada candidato
        self.__candCont2 = 0
        self.__candCont3 = 0
        self.__nulo = 0 # Contagem de votos nulos
        self.__branco = 0 # Contagem de votos em branco

    def brasil_melhor(self): # Função que não permite pessoas com QI negativo, ignorancia e falta de capacidade de participar das eleições
        while True:
            if self.__cand1 == "":
                print(f"\nDESCULPA, PERCEBEMOS QUE UM DE SEUS CANDIDATOS NAO TEM AS QUALIFICAÇÕES NECESSARIAS PARA SE ELEGER [bold red](CANDIDATO 1: {self.__cand1})[/] PENSE BEM ANTES DE VOTAR, [green]FAÇA SEU BRASIL UM BRASIL MELHOR[/green]!")
                exit()
            elif self.__cand2 == "":
                print(f"\nDESCULPA, PERCEBEMOS QUE UM DE SEUS CANDIDATOS NAO TEM AS QUALIFICAÇÕES NECESSARIAS PARA SE ELEGER [bold red](CANDIDATO 2: {self.__cand2})[/bold red], PENSE BEM ANTES DE VOTAR, [green]FAÇA SEU BRASIL UM BRASIL MELHOR[/green]!")
                exit()
            elif self.__cand3 == "":
                print(f"\nDESCULPA, PERCEBEMOS QUE UM DE SEUS CANDIDATOS NAO TEM AS QUALIFICAÇÕES NECESSARIAS PARA SE ELEGER [bold red](CANDIDATO 3: {self.__cand3})[/bold red], PENSE BEM ANTES DE VOTAR, [green]FAÇA SEU BRASIL UM BRASIL MELHOR[/green]!")
                exit()
            else:
                print("\nREGISTRANDO CANDIDATOS", end ="") # Caso o usuario coloquei candidatos qualificados
                sleep(0.5)
                print(".", end=""), sleep (0.5), print(".", end=""), sleep(0.5 ),print(".")
                print("\nCANDIDATOS REGISTRADOS, VAMOS COMEÇAR!")
                break
        
    def autoriza_voto(self, nasc): # Função que valida a idade do usuario
        year = date.today()
        nasc = year.year - nasc 
        if nasc < 16:
            nasc = 'SEU VOTO FOI [red]NEGADO[/red]'
            return nasc
        elif 16 <= nasc < 18  or nasc > 70:
            nasc = 'SEU VOTO É [green]OPCIONAL[/green]'
            return nasc
        else:
            nasc = 'SEU VOTO É [blue]OBRIGATORIO[/blue]'
            return nasc

    def votacao(self, autorizacao, voto): #Função que faz a validação dos votos, baseado se a pessoa pode ou nao votar
        while True:
            saida = str(input("\nDESEJA CADASTRAR MAIS UM VOTO? [S/N]: ")).upper().strip()[0]
            if saida == "N":
                print("OK, TENTE NOVAMENTE MAIS TARDE")
                break
            else:
                autorizacao = int(input("\nAno de nascimento: "))
                autorizacao = self.autoriza_voto(autorizacao)
                print(autorizacao)
                if autorizacao == "SEU VOTO FOI [red]NEGADO[/red]":
                    print("\nVOCÊ É MENOR DE IDADE E NAO PODE VOTAR") #Retorna a informação que menor de idade nao vota
                elif autorizacao == "SEU VOTO É [green]OPCIONAL[/green]":
                    confirmacao = str(input("\nDESEJA CONTINUAR COM O VOTO [S/N]: ")).upper().strip()[0] #Por ser Opcional, o usuario pode escolher se vota ou não
                    if confirmacao == "N":
                        print("\nOK, TENTE OUTRA HORA")
                        break
                    else:
                        print(f'''HORA DE VOTAR, ESCOLHA A OPÇÃO DESEJADA
        1 - [cyan]{self.__cand1}[/cyan]
        2 - [blue]{self.__cand2}[/blue]
        3 - [purple]{self.__cand3}[/purple]
        4 - [yellow]Voto Nulo[/yellow]
        5 - [white]Voto em Branco[/white]''')
                        voto = int(input("OPÇÃO: "))
                        if voto == 1:
                            self.__candCont1 += 1
                        elif voto == 2:
                            self.__candCont2 += 1
                        elif voto == 3:
                            self.__candCont3 += 1
                        elif voto == 4:
                            self.__nulo += 1
                        elif voto == 5:
                            self.__branco += 1
                        else:
                            print("[red]OPÇÃO INVALIDA[/red]")
                else: #Else se caso a pessoa for Obrigatoria a votar, nao tem a opção de escolher se vota ou não
                    print(f'''HORA DE VOTAR, ESCOLHA A OPÇÃO DESEJADA
        1 - [cyan]{self.__cand1}[/cyan]
        2 - [blue]{self.__cand2}[/blue]
        3 - [purple]{self.__cand3}[/purple]
        4 - [yellow]Voto Nulo[/yellow]
        5 - [white]Voto em Branco[/white]''')
                    voto = int(input("OPÇÃO: "))
                    if voto == 1:
                        self.__candCont1 += 1
                    elif voto == 2:
                        self.__candCont2 += 1
                    elif voto == 3:
                        self.__candCont3 += 1
                    elif voto == 4:
                        self.__nulo += 1
                    elif voto == 5:
                        self.__branco += 1
                    else:
                        print("OPÇÃO INVALIDA")

        with Progress() as progress: #Barras de progresso para apuração dos votos
            task1 = progress.add_task("[red]Apurando Votos da Regiao Sul...", total=500)
            task2 = progress.add_task("[blue]Apurando Votos da Regiao Sudeste...", total=500)
            task3 = progress.add_task("[green]Apurando Votos da Regiao Nordeste...", total=500)
            task4 = progress.add_task("[yellow]Apurando Votos da Regiao Norte...", total=500)
            task5 = progress.add_task("[cyan]Apurando Votos da Regiao Centro-Oeste...", total=500)
            while not progress.finished:
                progress.update(task1, advance=0.8)
                progress.update(task2, advance=1)
                progress.update(task3, advance=0.6)
                progress.update(task4, advance=0.9)
                progress.update(task5, advance=0.7)
                time.sleep(0.005)
                
        print("\n[cyan]APÓS APURAÇÃO DOS VOTOS TEMOS O RESULTADO[/cyan]\n")
        sleep(1)
        if self.__candCont1 > self.__candCont2 and self.__candCont1 > self.__candCont3: #Condições que validam qual candidato tem mais votos, e apresenta o vencedor
            print(f'{self.__cand1} [green]VENCEU AS ELEIÇÕES[/green] COM {self.__candCont1} VOTOS')
        elif self.__candCont2 > self.__candCont1 and self.__candCont2 > self.__candCont3:
            print(f'{self.__cand2} [green]VENCEU AS ELEIÇÕES[/green] COM {self.__candCont2} VOTOS')
        elif self.__candCont3 > self.__candCont1 and self.__candCont3 > self.__candCont2:
            print(f'{self.__cand3} [green]VENCEU AS ELEIÇÕES[/green] COM {self.__candCont3} VOTOS')

    def __str__(self): #Aprensentação de todos os votos
       return f'''\nQUANTIDADES DE VOTOS
        1 - {self.__cand1}: {self.__candCont1} VOTOS
        2 - {self.__cand2}: {self.__candCont2} VOTOS
        3 - {self.__cand3}: {self.__candCont3} VOTOS
        4 - VOTO NULO: {self.__nulo} VOTOS
        5 - VOTO EM BRANCO: {self.__branco} VOTOS
        '''