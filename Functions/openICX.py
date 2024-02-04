from imports import *
def abrir_ixc(driver, janela):

    checkbox_play = tk.BooleanVar()
    checkbox_voip = tk.BooleanVar()

    driver.get("https://ixc.hipervi.com.br/adm.php")
    # time.sleep(100)
    driver.find_element('xpath' , '/html/body/div[3]/div/div[4]/form/div[2]/input').send_keys(login)
    driver.find_element('id' , '/html/body/div[3]/div/div[4]/form/div[3]/input').send_keys( senha + Keys.RETURN )

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
    
    if   int(plano) == 100 : driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '79' + Keys.TAB )
    elif int(plano) == 200 : driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '71' + Keys.TAB )
    elif int(plano) == 400 : driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '29' + Keys.TAB )
    elif int(plano) == 500 : driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '80' + Keys.TAB )           
    elif int(plano) == 700 : driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '68' + Keys.TAB )
                        
    if   int(vencimento) == 5  : driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '05' + Keys.TAB )
    elif int(vencimento) == 10 : driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '10' + Keys.TAB )
    elif int(vencimento) == 15 : driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '15' + Keys.TAB )
    elif int(vencimento) == 20 : driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '20' + Keys.TAB )
    elif int(vencimento) == 25 : driver.find_element('xpath', '//*[@id="id_tipo_contrato"]').send_keys( '25' + Keys.TAB )

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
    



    if   int(plano) == 100 : driver.find_element('xpath', '//*[@id="id_grupo"]').send_keys( '77' + Keys.TAB )
    elif int(plano) == 200 : driver.find_element('xpath', '//*[@id="id_grupo"]').send_keys( '71' + Keys.TAB )            
    elif int(plano) == 400 : driver.find_element('xpath', '//*[@id="id_grupo"]').send_keys( '27' + Keys.TAB )                
    elif int(plano) == 500 : driver.find_element('xpath', '//*[@id="id_grupo"]').send_keys( '64' + Keys.TAB )                       
    elif int(plano) == 700 : driver.find_element('xpath', '//*[@id="id_vd_contrato"]').send_keys( '68' + Keys.TAB )

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
