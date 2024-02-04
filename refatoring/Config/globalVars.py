from imports import *

## feito assim para facilitar a visualizacao
global nome , cpf_formatado , nascimento_formatado , telefone_formatado , telefone2_formatado
global cep_formatado , numero_casa , complemento, plano , vencimento, tel_numeros, email
global filial, data_ativacao_formatado , data_financeiro_formatado ,  data_renovacao_formatado
global pppoe, bl, ap, login, senha, cpf_numeros, n_condominio, entries, inputs, options_crm
global mapeamento_crm, options_condominio, mapeamento_condominio, n_crm, resultado_label, valores

cpf_numeros = ""

n_condominio = None

entries = []

valores = []

inputs = ['Nome Completo' , 'CPF', 'Data de Nascimento', 'CEP','Numero da casa', '', 'Bloco', 'Apartamento', 'Telefone Celular' , 'Telefone Residencial' , 'E-mail' ,
    'Plano desejado', 'Data de vencimento da fatura', 'Filial' , "Pppoe"]

options_crm = [
    ("Equipe Comercial", 6), ("Solicitado pelo Cliente", 1),
    ("Pos-Venda Belluno", 21), ("Pesquisou no Google", 2),
    ("Instagram", 10), ("Indicacao", 4), ("Flyer", 15),
    ("Feiras", 7), ("Facebook", 3), ("Eventos", 19),
    ("Equipe tecnica", 13), ("Equipe de Instalacoes", 12),
    ("Eletromidia", 17), ("Contato por e-mail", 5),
    ("Contato pelo Chat", 8), ("Acoes Tv", 11)
]


mapeamento_crm = dict(options_crm)


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

mapeamento_condominio = dict(options_condominio)