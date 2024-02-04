# imports de bibliotecas
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import time, pyautogui, tkinter as tk, importlib

#imports de configs
from Config.globalVars import *
from Config.installLibs import installLibs
from Config.tkSetup import tkSetup
from Config.webdriverSetup import webdriverSetup

#imports de funções
from Functions.minimizeTk import minimizeTk
from Functions.getInputs import getInputs
from Functions.getCondominio import getCondominio
from Functions.inputDados import input_dados
from Functions.getValorAssociado import getValorAssociado
from Functions.openICX import abrir_ixc