"""
Módulo de automação de interface.

Este módulo contém uma classe com seus respectivos métodos para gerenciar a interação com o navegador
e utilizando RPA.
"""

from typing import Union, List
import pyautogui

class BroswerScript:
    """
    Esta classe utiliza a biblioteca PyAutoGUI para simular interações de hardware.

    Attributes:
        pyautogui.PAUSE (float): Define o intervalo global entre comandos.
    """

    pyautogui.PAUSE = 1

    def command_press(self, key: str) -> None:
        """
        Pressiona uma tecla específica seguido de um intervalo.

        Args:
            key (str): O nome da tecla a ser pressionada (ex: 'enter', 'tab').
        """
        pyautogui.press(key)
       
    def command_write(self, text: str) -> None:
        """
        Simula a digitação de uma string de texto.

        Args:
            text (str): O conteúdo textual a ser inserido no campo focado.
        """
        pyautogui.write(text)

    def command_click(self, x_y: Union[tuple, str]) -> None:
        """
        Executa um evento de clique do mouse em coordenadas ou elemento visual.

        Args:
            x_y (Union[tuple, str]): Coordenadas (x, y) ou caminho para imagem de 
                referência para o clique.
        """
        pyautogui.click(x_y)

    def command_hotkey(self, keys: List[str]) -> None:
        """
        Executa uma combinação de teclas de atalho simultâneas.

        Args:
            keys (List[str]): Lista de strings representando as teclas (ex: ['ctrl', 'v']).
        """
        pyautogui.hotkey(*keys)
