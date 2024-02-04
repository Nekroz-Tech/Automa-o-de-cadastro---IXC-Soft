from imports import *

def getCondominio(resultado_label):
    
    escolha_condominio = condominio_lista.get()
    if escolha_condominio in mapeamento_condominio:
        n_condominio = mapeamento_condominio[escolha_condominio]
        resultado_label.config(text=str(n_condominio))
        return n_condominio
