import importlib

# Bibliotecas a serem verificadas
libs_to_check = ['time', 'pyautogui', 'tkinter', 'selenium', 'webdriver_manager', 'selenium.webdriver.chrome.service']

# Verifique e instale as bibliotecas ausentes
for lib in libs_to_check:
    try:
        importlib.import_module(lib)
    except ImportError:
        print(f"{lib} não está instalado. Instalando...")
        try:
            if lib == 'selenium.webdriver.chrome.service':
                # Tratamento especial para 'selenium.webdriver.chrome.service'
                from selenium.webdriver.chrome.service import Service
            else:
                # Instalação padrão para outras bibliotecas
                import pip
                pip.main(['install', lib])
        except Exception as e:
            print(f"Falha ao instalar {lib}: {str(e)}")
        else:
            print(f"{lib} instalado com sucesso!")

# Agora você pode usar as bibliotecas normalmente no restante do seu código

import time
import pyautogui
import tkinter as tk

#---------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#python -m PyInstaller --onefile Automacao_Cad_IX-Soft.py







#imports
#---------------------------------------------------------------

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

driver.implicitly_wait(10)  



janela = Tk()
janela.title('Cadastro automatico de clientes')

def minimize():
    janela.iconify()
    
checkbox_play = tk.BooleanVar()
checkbox_voip = tk.BooleanVar()
    
Label(janela, text='PREENCHA OS DADOS DO CLIENTE').grid(column=0, row=0)

inputs = ['Nome Completo' , 'CPF', 'Data de Nascimento', 'CEP','Numero da casa', '', 'Bloco', 'Apartamento', 'Telefone Celular' , 'Telefone Residencial' , 'E-mail' ,
          'Plano desejado', 'Data de vencimento da fatura', 'Filial' , "Pppoe"]

cpf_numeros = ""

n_condominio = None

                
def obter_inputs():
    global nome , cpf_formatado , nascimento_formatado , cep_formatado , telefone_formatado , telefone2_formatado, cep_formatado , numero_casa , complemento, plano , vencimento, tel_numeros, email, filial, data_ativacao_formatado , data_financeiro_formatado ,  data_renovacao_formatado , pppoe, bl, ap, login, senha
    valores = []
    for entry in entries:
        valores.append(entry.get())
        
    nome = (entries[0].get())
    cpf = (entries[1].get())
    nascimento = (entries[2].get())
    cep = (entries[3].get())
    numero_casa = (entries[4].get())
    bl = (entries[6].get())
    ap = (entries[7].get())
    telefone = (entries[8].get())
    telefone2 = (entries[9].get())
    email = (entries[10].get())
    plano = (entries[11].get())
    vencimento = (entries[12].get())
    filial = (entries[13].get())
    pppoe = (entries[14].get())
    login = entry_login.get()
    senha = entry_senha.get()
    
    #formatacoes
    
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) == 11:
        cpf_formatado = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    
    nascimento = ''.join(filter(str.isdigit, nascimento))
    if len(nascimento) == 8:
        nascimento_formatado = "{} / {} / {}".format(nascimento[:2], nascimento[2:4], nascimento[4:])    
    
    cep = ''.join(filter(str.isdigit, cep))
    if len(cep) == 8:
        cep_formatado = "{}-{}".format(cep[:5], cep[5:])
        
    telefone = ''.join(filter(str.isdigit, telefone))
    if len(telefone) >= 10:
        telefone_formatado = "({}) {}-{}".format(telefone[:2], telefone[2:6], telefone[6:11])
        
    if telefone2:
        telefone2 = ''.join(filter(str.isdigit, telefone2))
        if len(telefone2) >= 10:
            telefone2_formatado = "({}) {}-{}".format(telefone2[:2], telefone2[2:6], telefone2[6:11])

resultado_label = Label(janela, text="")

    
options_condominio = [
    ("", None ),
    ("Alianca Park", 112),
    ("America Mbigucci, California", 87),
    ("America Mbigucci, Florida", 121),
    ("Amazonas, Bl 01", 21),
    ("Amazonas, Bl 10", 20),
    ("Amazonas, Bl 13", 23),
    ("Amazonas, Bl 14", 22),
    ("Amazonas, Bl 15", 32),
    ("Amazonas, Bl 16", 30),
    ("Amazonas, Bl 17", 31),
    ("Amazonas, Bl 18", 34),
    ("Amazonas, Bl 19", 40),
    ("Amazonas, Bl 02", 17),
    ("Amazonas, Bl 20", 24),
    ("Amazonas, Bl 03", 35),
    ("Amazonas, Bl 04", 18),
    ("Amazonas, Bl 09", 19),
    ("Amarilis", 29),
    ("Avila", 1),
    ("Barcelona", 7),
    ("Barroco", 72),
    ("Bela Vista", 91),
    ("Bilbao", 5),
    ("California", 38),
    ("Ceuta", 6),
    ("Conj. Hab. Sao Bernardo do Campo S2, - LOTE 1A", 119),
    ("Conquista - area 05", 79),
    ("Dona Nazare", 71),
    ("Elba", 15),
    ("Estrela Azul", 104),
    ("Fabiana e Daniele", 77),
    ("Feltrins Gold Bl 1", 59),
    ("Feltrins Gold Bl 2", 60),
    ("Feltrins Gold Bl 3", 61),
    ("Florestan Fernandes", 14),
    ("Granja Ito", 73),
    ("Ibiza", 11),
    ("Ibirapita Interlagos", 16),
    ("Ieda Luiza de Souza, 210", 42),
    ("Ieda Luiza de Souza, 230", 43),
    ("Ieda Luiza de Souza, 270", 44),
    ("Ieda Luiza de Souza, 290", 45),
    ("Ieda Luiza de Souza, 310", 46),
    ("Ieda Luiza de Souza, 350", 48),
    ("Ilha dos Acores", 108),
    ("Independencia", 2),
    ("Isabela", 27),
    ("Jardim Martini", 33),
    ("Jk, area 1", 83),
    ("Josef Juedel Naftal", 99),
    ("Leao", 8),
    ("Madrid", 9),
    ("Mario Lago", 28),
    ("Melila", 10),
    ("Morada do Sol", 106),
    ("Nossa Senhora do Sabara", 26),
    ("Novo horizone", 95),
    ("Osvaldo Cruz - area 2", 85),
    ("Pamplona", 4),
    ("Paraiso", 118),
    ("Pompeia", 116),
    ("Porto Real", 36),
    ("Porto Seguro", 39),
    ("Raio de Luz", 110),
    ("Redentor - area 4", 75),
    ("Rios", 66),
    ("Rios, torre A", 68),
    ("Rios, torre B", 69),
    ("Rios, torre C", 67),
    ("Rios, torre D", 70),
    ("Sagrada Familia, Bl 1", 53),
    ("Sagrada Familia, Bl 2", 54),
    ("Sagrada Familia, Bl 3", 55),
    ("Santa Clara", 93),
    ("Santo Dias da Silva BL 01", 49),
    ("Santo Dias da Silva BL 02", 50),
    ("Santo Dias da Silva BL 03", 51),
    ("Santo Dias da Silva BL 04", 52),
    ("Solaris Zunta", 41),
    ("Styllo", 97),
    ("Topazio Zafira Rubi, Bl 1", 56),
    ("Topazio Zafira Rubi, Bl 2", 57),
    ("Topazio Zafira Rubi, Bl 3", 58),
    ("Tres Marias (Beta Dragone)", 65),
    ("Tres Marias (Centauro)", 63),
    ("Tres Marias (Ceu Azul)", 62),
    ("Tres Marias (Rua Constelacao)", 64),
    ("Uniao das Flores", 89),
    ("Valencia", 13),
    ("Vitoria - area 3", 114),
    ("Vitoria Regia", 3),
    ("Vitoria", 12),
    ("Villagio di San Remo", 37),
]


def obter_condominio():
    global n_condominio
    escolha_condominio = condominio_lista.get()
    if escolha_condominio in mapeamento_condominio:
        n_condominio = mapeamento_condominio[escolha_condominio]
        resultado_label.config(text=str(n_condominio))
        return n_condominio
    
options_crm = [
    ("Equipe Comercial", 6), ("Solicitado pelo Cliente", 1),
    ("Pos-Venda Belluno", 21), ("Pesquisou no Google", 2),
    ("Instagram", 10), ("Indicacao", 4), ("Flyer", 15),
    ("Feiras", 7), ("Facebook", 3), ("Eventos", 19),
    ("Equipe tecnica", 13), ("Equipe de Instalacoes", 12),
    ("Eletromidia", 17), ("Contato por e-mail", 5),
    ("Contato pelo Chat", 8), ("Acoes Tv", 11)
]

mapeamento_condominio = dict(options_condominio)

mapeamento_crm = dict(options_crm)


def obter_valor_associado():
    global n_crm
    escolha_crm = crm_lista.get()
    if escolha_crm in mapeamento_crm:
        n_crm = mapeamento_crm[escolha_crm]
        resultado_label.config(text=str(n_crm))
        return n_crm

def input_dados(janela, text, row, column):
    Label(janela, text = text).grid(column=column, row=row)
    entry = Entry(janela)
    entry.grid(column=column+1, row=row)
    return entry

def abrir_ixc():
    driver.get("https://ixc.hipervi.com.br/adm.php")
    driver.find_element('xpath' , '//*[@id="email"]').send_keys( login)
    driver.find_element('xpath' , '//*[@id="senha"]').send_keys( senha + Keys.RETURN )
#CADASTRO
    driver.find_element('xpath', '//*[@id="menu04400d48d04acd3599cf545dafbb90ed"]/div/a').click()
    driver.find_element('xpath', '//*[@id="grupo_menu04400d48d04acd3599cf545dafbb90ed"]/ul/li[1]/a').click()
    driver.find_element('xpath', '//*[@id="1_grid"]/div/div[2]/div[1]/button[1]').click()
    driver.find_element('xpath', '//*[@id="id_tipo_cliente"]').send_keys( '6' + Keys.TAB )
    driver.find_element('xpath', '//*[@id="razao"]').send_keys( nome + Keys.TAB)
    driver.find_element('xpath', '//*[@id="fantasia"]').send_keys( nome + Keys.TAB)
    driver.find_element('xpath', '//*[@id="cnpj_cpf"]').click()
    driver.find_element('xpath', '//*[@id="cnpj_cpf"]').send_keys( cpf_formatado + Keys.TAB )
    driver.find_element('xpath', '//*[@id="data_nascimento"]').click()
    driver.find_element('xpath', '//*[@id="data_nascimento"]').click()
    driver.find_element('xpath', '//*[@id="data_nascimento"]').send_keys( nascimento_formatado )
    driver.find_element('xpath', '//*[@id="filial_id"]').clear()
    driver.find_element('xpath', '//*[@id="filial_id"]').send_keys( filial + Keys.TAB )
    driver.find_element('xpath', '//*[@id="2_form"]/div[3]/ul/li[2]/a').click()
    time.sleep(1)
    
    if n_condominio is not None:
            driver.find_element('xpath', '//*[@id="id_condominio"]').send_keys( n_condominio )
            driver.find_element('xpath', '//*[@id="bloco"]').send_keys( bl )
            driver.find_element('xpath', '//*[@id="apartamento"]').send_keys( ap )
    else :
        driver.find_element('xpath', '//*[@id="cep"]').send_keys( cep_formatado )
        driver.find_element('xpath', '//*[@id="buscacep"]').click()
        driver.find_element('xpath', '//*[@id="numero"]').send_keys( numero_casa )
    driver.find_element('xpath', '//*[@id="2_form"]/div[3]/ul/li[3]/a').click()
    try:
        if telefone2_formatado is not None :
            driver.find_element('xpath', '//*[@id="fone"]').send_keys( telefone2_formatado )
            driver.find_element('xpath', '//*[@id="telefone_celular"]').send_keys( telefone_formatado )
    except NameError:
        driver.find_element('xpath', '//*[@id="telefone_celular"]').send_keys( telefone_formatado )
    try:
        if email is not None :
            driver.find_element('xpath', '//*[@id="email"]').send_keys( email )
            driver.find_element('xpath', '//*[@id="2_form"]/div[3]/ul/li[4]/a').click()
    except NameError:
        driver.find_element('xpath', '//*[@id="2_form"]/div[3]/ul/li[4]/a').click()    
    time.sleep(1)
    driver.find_element('xpath', '//*[@id="crmS"]').click()
    driver.find_element('xpath', '//*[@id="id_candato_tipo"]').send_keys( n_crm  )
    driver.find_element('xpath', '//*[@id="id_campanha"]').click()
    driver.find_element('xpath', '//*[@id="2_form"]/div[2]/button[3]').click() #salvar
    
    #CONTRATO 
    driver.find_element('xpath', '//*[@id="2_form"]/div[3]/ul/li[7]/a').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/form[2]/div[3]/div[7]/dl/div/div/div[2]/div[1]/button[1]').click()
    
    time.sleep(1)
    
    if int(plano) == 100 :
        driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '79' + Keys.TAB )
    else :
        if int(plano) == 200 :
            driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '71' + Keys.TAB )
        else :
            if int(plano) == 400 :
                driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '29' + Keys.TAB )
            else :
                if int(plano) == 500 :
                    driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '80' + Keys.TAB )
    
                else :
                    if int(plano) == 700 :
                        driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '68' + Keys.TAB )
    if int(vencimento) == 5 :
        driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '05' + Keys.TAB )
    if int(vencimento) == 10 :
        driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '10' + Keys.TAB )
    if int(vencimento) == 15 :
        driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '15' + Keys.TAB )
    if int(vencimento) == 20 :
        driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '20' + Keys.TAB )
    if int(vencimento) == 25 :
        driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '25' + Keys.TAB )
        
    if int(filial) == 1 :
        if checkbox_play.get():   
            driver.find_element('xpath', '//*[@id="id_modelo"]').send_keys( '28' + Keys.TAB )
            if checkbox_voip.get():
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys( "ONT Huawei em comodato + Izy Play" )
                driver.find_element('xpath', '//*[@id="contrato"]').send_keys( " + 1 ponto Nave Play por R$70,00 + Voip por R$20,00" )
            else :
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys( "Huawei Ax2 em comodato + Izy Play" )
                driver.find_element('xpath', '//*[@id="contrato"]').send_keys( " + 1 ponto Nave Play por R$70,00")
        else :
            driver.find_element('xpath', '//*[@id="id_modelo"]').send_keys( '4' + Keys.TAB )
        if checkbox_voip.get():
            if checkbox_play.get():
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys( "" )
            else :
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys( "ONT Huawei em comodato" )
                driver.find_element('xpath', '//*[@id="contrato"]').send_keys( " + Voip por R$30,00" )
        else :
            if checkbox_play.get():
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys( "" )
            else :
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys( "Huawei Ax2 em comodato" )
        
    #PARA NOVA WEB
    else :
        if checkbox_play.get():
            driver.find_element('xpath', '//*[@id="id_modelo"]').send_keys('31' + Keys.TAB)
            if checkbox_voip.get():
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys("ONT Huawei em comodato + Izy Play")
                time.sleep(1)
                driver.find_element('xpath', '//*[@id="contrato"]').send_keys(" + 1 ponto Nave Play por R$70,00 + Voip por R$20,00")
            else :
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys("Huawei Ax2 em comodato + Izy Play")
                time.sleep(1)
                driver.find_element('xpath', '//*[@id="contrato"]').send_keys(" + 1 ponto Nave Play por R$70,00")
        else :
            driver.find_element('xpath', '//*[@id="id_modelo"]').send_keys('12' + Keys.TAB)        
            if checkbox_voip.get():
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys( "ONT Huawei em comodato" )
                driver.find_element('xpath', '//*[@id="contrato"]').send_keys( " + Voip por R$30,00" )
            else :
                driver.find_element('xpath', '//*[@id="descricao_aux_plano_venda"]').send_keys( "Huawei Ax2 em comodato" )
        driver.find_element('xpath', '//*[@id="id_filial"]').clear()
        driver.find_element('xpath', '//*[@id="id_filial"]').send_keys( '2' + Keys.TAB )
        driver.find_element('xpath', '//*[@id="3_form"]/div[3]/ul/li[2]/a').click()
        driver.find_element('xpath', '//*[@id="id_carteira_cobranca"]').clear()
        driver.find_element('xpath', '//*[@id="id_carteira_cobranca"]').send_keys ( '9' + Keys.TAB)
        time.sleep(1)
    driver.find_element('xpath', '//*[@id="3_form"]/div[3]/ul/li[3]/a').click()
    driver.find_element('xpath', '//*[@id="desconto_fidelidade"]').send_keys( '250,00' + Keys.TAB )
    driver.find_element('xpath', '/html/body/form[3]/div[2]/button[2]').click()
    
    #ADD NAVE PLAY
    if checkbox_play.get():
        driver.find_element('xpath', '//*[@id="3_form"]/div[3]/ul/li[7]/a').click()
        driver.find_element('xpath', '//*[@id="6"]/dl/div/div/div[2]/div[1]/button[1]').click()
        driver.find_element('xpath', '//*[@id="4_form"]/div[3]/ul/li[1]/a').click()
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('right')
        driver.find_element('xpath', '//*[@id="id_produto"]').send_keys( "116" + Keys.TAB )
        driver.find_element('xpath', '//*[@id="qtde"]').clear()
        driver.find_element('xpath', '//*[@id="qtde"]').send_keys( '1' + Keys.TAB )
        driver.find_element('xpath', '//*[@id="4_form"]/div[2]/button[1]').click()
        driver.find_element('xpath', '//*[@id="3_form"]/div[2]/button[2]').click()
        
    #ADD VOIP
    if checkbox_voip.get():
        driver.find_element('xpath', '//*[@id="3_form"]/div[3]/ul/li[7]/a').click()
        driver.find_element('xpath', '//*[@id="6"]/dl/div/div/div[2]/div[1]/button[1]').click()
        driver.find_element('xpath', '//*[@id="4_form"]/div[3]/ul/li[1]/a').click()
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('right') 
        driver.find_element('xpath', '//*[@id="id_produto"]').send_keys( "75" + Keys.TAB )
        driver.find_element('xpath', '//*[@id="qtde"]').clear()
        driver.find_element('xpath', '//*[@id="qtde"]').send_keys( '1' + Keys.TAB )
        driver.find_element('xpath', '//*[@id="valor_unit"]').clear()
        driver.find_element('xpath', '//*[@id="valor_unit"]').send_keys( '30,00' )
        driver.find_element('xpath', '//*[@id="4_form"]/div[2]/button[1]').click()
        
           
    driver.find_element('xpath', '//*[@id="cliente_contrato_btn_close"]').click()

    #login
    driver.find_element('xpath', '//*[@id="2_form"]/div[3]/ul/li[8]/a').click()
    time.sleep(1)
    driver.find_element('xpath', '//*[@id="10"]/dl/div/div/div[3]/div[1]/button[1]').click()
    time.sleep(1)
    
    if int(plano) == 100 :
        driver.find_element('xpath', '//*[@id="id_grupo"]').send_keys( '77' + Keys.TAB )
    else :
        if int(plano) == 200 :
            driver.find_element('xpath', '//*[@id="id_grupo"]').send_keys( '71' + Keys.TAB )
        else :
            if int(plano) == 400 :
                driver.find_element('xpath', '//*[@id="id_grupo"]').send_keys( '27' + Keys.TAB )
            else :
                if int(plano) == 500 :
                    driver.find_element('xpath', '//*[@id="id_grupo"]').send_keys( '64' + Keys.TAB )
                 
                else :
                    if int(plano) == 700 :
                        driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '68' + Keys.TAB )
    
    driver.find_element('xpath', '//*[@id="login"]').send_keys( pppoe )
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.press('return')









    janela.mainloop()

def bind_enter(event):
    obter_inputs()
    abrir_ixc()
    minimize()

entries = []
for i, dado in enumerate(inputs):
    entry = input_dados(janela, dado, i+1, 0)
    entries.append(entry)
    entry.bind("<Return>", bind_enter)
    
for entry in entries:
    entry.bind("<Return>", bind_enter)
   
botao_confirmar = Button(janela , width=20, text='Confirmar Cadastro', command=lambda:[ minimize(), obter_inputs(), obter_valor_associado(), obter_condominio(), abrir_ixc()] )
botao_confirmar.grid(column=1, row=22)

Label(janela, text="CRM").grid(column =0, row=16)
crm_lista = ttk.Combobox(janela, values=[opcao[0] for opcao in options_crm], width=20)
crm_lista.grid(column=1, row=16)

Label(janela, text="Condominio").grid(column =0, row=6)
condominio_lista = ttk.Combobox(janela, values=[opcao[0] for opcao in options_condominio], width=25)
condominio_lista.grid(column=1, row=6)

Label(janela, text="Nave Play").grid(column =0, row=20)
Label(janela, text="Voip").grid(column =0, row=21)
tk.Checkbutton(janela, variable=checkbox_play).grid(column=1, row=20)
tk.Checkbutton(janela, variable=checkbox_voip).grid(column=1, row=21)

Label(janela, text='Antes de colocar o auto preenchimento, confirme se o nome do cliente confere com o CPF no site da receita federal.').grid(column=0, row=25)
Label(janela, text='O contrato e preenchido com fidelidade por padrao, se houver necessidade de adicionar Nave Play ou Voip manualmente').grid(column=0, row=26)
Label(janela, text='Assinatura precisa ser colocada no status "aguardando" manualmente').grid(column=0, row=28)
Label(janela, text='O contrato e preenchido sempre com fidelidade, se nao houver, e necessario colocar trocar o tipo do contrato manualmente. Tambem Conferir na planilha de condominios quais nao possuem fidelidade').grid(column=0, row=29)
Label(janela, text='O Nave Play e preenchido com plano Mix, inserir Max manualmente. Se inserir plano com Tv/Voip, não minimizar a tela').grid(column=0, row=30)


def limpar_campos():
    for entry in entries:
        entry.delete(0, END)

    
    #del n_condominio
    # Limpar o valor selecionado no Combobox
    condominio_lista.set("")
    # Garantir que o estado do Combobox seja atualizado
    condominio_lista['values'] = [opcao[0] for opcao in options_condominio]
    
    #del n_crm
    # Limpar o valor selecionado no Combobox
    crm_lista.set("") 
    # Garantir que o estado do Combobox seja atualizado
    crm_lista['values'] = [opcao[0] for opcao in options_crm]

    crm_lista.set("")  # Limpar o valor selecionado no Combobox
    
    checkbox_play.set(False)
    checkbox_voip.set(False)



botao_limpar = Button(janela, width=20, text='Limpar Campos', command=limpar_campos)
botao_limpar.grid(column=1, row=23)

Label(janela, text='Login IXC', width=20).grid(column=0, row=34)
entry_login = Entry(janela)
entry_login.grid(column=1, row=34)

Label(janela, text='Senha IXC', width=20).grid(column=0, row=35)
entry_senha = Entry(janela, show='')  # Use show='' para ocultar a senha
entry_senha.grid(column=1, row=35)

Label(janela, text='').grid(column=0, row=36)

Label(janela, text='').grid(column=0, row=32)

janela.mainloop()
