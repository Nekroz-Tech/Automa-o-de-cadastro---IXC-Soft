from imports import *

def getValorAssociado():
    escolha_crm = crm_lista.get()
    if escolha_crm in mapeamento_crm:
        n_crm = mapeamento_crm[escolha_crm]
        resultado_label.config(text=str(n_crm))
        return n_crm