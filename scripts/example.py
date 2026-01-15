"""
Script de Exemplo.

Este script exemplifica a aplicação prática da biblioteca PyAutoGUI para o 
desafio da Jornada Python (Hashtag Programação). Ele automatiza o fluxo 
desde a abertura do navegador até o cadastro cíclico de produtos.

Observação: Este arquivo contém configurações específicas para o ambiente 
local utilizado pelo desenvolvedor.
"""

import time
import pandas as pd
import pyautogui 
from powerup.inteface_script import InterfaceScript
from powerup.DatasetManager import DataSet

"""
Executa o ciclo completo de automação para o desafio de cadastro.
"""
# Configurações iniciais
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Instancia do script para interface
automation = InterfaceScript()

try:
    # --- Passo 1: Acesso ao Navegador ---
    automation.command_press("win")
    automation.command_write("chrome")
    automation.command_press("enter")
    time.sleep(3)
    
    # Navegação por abas/perfis do Chrome (ajustar conforme necessidade local)
    automation.command_press("tab")
    automation.command_press("enter")

    # --- Passo 2: Login no Sistema ---
    automation.command_hotkey(["ctrl", "shift", "n"])  # Janela anônima
    automation.command_write(link)
    automation.command_press("enter")
    time.sleep(3)  # Aguarda carregamento do site

    # Preenchimento de credenciais
    automation.command_press("tab")
    automation.command_write("cadastro@cadastro.com")
    automation.command_press("tab")
    automation.command_write("cadastrosenha")
    automation.command_press("enter")
    time.sleep(3)  # Aguarda redirecionamento para o formulário

    # --- Passo 3: Processamento de Dados ---
    db_manager = DataSet()
    tabela = db_manager.read_dataset("data/produtos.csv")

    # --- Passo 4: Calibração de Interface ---
    print("Calibração: Posicione o mouse no primeiro campo do formulário.")
    time.sleep(5)
    # Captura a posição inicial para resetar o foco a cada loop
    posicao_inicial = automation.get_position_mouse()

    # --- Passo 5: Loop de Cadastro ---
    for linha in tabela.index:
        # Retorna o foco para o início do formulário
        automation.command_click(posicao_inicial)

        # Extração de dados da linha atual
        codigo = str(tabela.loc[linha, "codigo"])
        marca = str(tabela.loc[linha, "marca"])
        tipo = str(tabela.loc[linha, "tipo"])
        categoria = str(tabela.loc[linha, "categoria"])
        preco = str(tabela.loc[linha, "preco_unitario"])
        custo = str(tabela.loc[linha, "custo"])
        obs = tabela.loc[linha, "obs"]

        # Sequência de preenchimento automatizado
        automation.command_write(codigo)
        automation.command_press("tab")
        automation.command_write(marca)
        automation.command_press("tab")
        automation.command_write(tipo)
        automation.command_press("tab")
        automation.command_write(categoria)
        automation.command_press("tab")
        automation.command_write(preco)
        automation.command_press("tab")
        automation.command_write(custo)
        automation.command_press("tab")

        # Tratamento de campos opcionais (Observação)
        if not pd.isna(obs):
            automation.command_write(str(obs))

        # Submissão do formulário
        automation.command_press("tab")
        automation.command_press("enter")

        # Scroll para voltar ao inicio da tela  
        automation.command_scroll(5000)

except pyautogui.FailSafeException:
    print("\n[ALERTA] Execução interrompida pelo usuário (Fail-Safe acionado).")

except Exception as error:
    print(f"\n[ERRO] Ocorreu uma falha inesperada: {error}")
