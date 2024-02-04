from imports import *

def getInputs():
    for entry in entries:
        valores.append(entry.get())
        
    nome           =  (entries[0].get())
    cpf            =  (entries[1].get())
    nascimento     =  (entries[2].get())
    cep            =  (entries[3].get())
    numero_casa    =  (entries[4].get())
    bl             =  (entries[6].get())
    ap             =  (entries[7].get())
    telefone       =  (entries[8].get())
    telefone2      =  (entries[9].get())
    email          =  (entries[10].get())
    plano          =  (entries[11].get())
    vencimento     =  (entries[12].get())
    filial         =  (entries[13].get())
    pppoe          =  (entries[14].get())

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
