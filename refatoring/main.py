from imports import *

class Main():
    # inicia o programa verificando as bibliotecas necessárias
    def install():
        installLibs()

    def __init__(self):
        #chama as funções de configuração de webdriver e tkinter
        janela = tkSetup()
        driver = webdriverSetup()

        #minimiza a tela do tk
        minimizeTk()

        #define a label da janela
        Label(janela, text='PREENCHA OS DADOS DO CLIENTE').grid(column=0, row=0)
        ## revisar fluxo a partir daqui ##
        #chama a função para pegar os inputs do usuário      
        getInputs()

        # função para pegar qual o condominio
        resultado_label = Label(janela, text="")
        getCondominio(resultado_label)

        inputDados(janela, text, row, column)

        abrir_ixc(driver, janela)

Main()