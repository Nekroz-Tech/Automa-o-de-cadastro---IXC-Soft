from imports import *

def installLibs():
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
