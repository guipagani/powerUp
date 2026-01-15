"""
Módulo de automação de interface para fluxos de RPA.

Este módulo implementa a classe InterfaceScript, que fornece abstrações para
comandos da biblioteca PyAutoGUI.
"""

from typing import Union, List
from powerup.position_mouse import PositionMouse
import pyautogui

class InterfaceScript(PositionMouse):
    """
    Abstração para simulação de interações de hardware via PyAutoGUI.

    Herda funcionalidades de PositionMouse para mapeamento de coordenadas e
    estende as capacidades de interação com teclado, mouse e scroll.

    Attributes:
        PAUSE (float): Intervalo global de espera definido no PyAutoGUI.
    """

    # Configuração de latência global entre comandos
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 1

    def command_press(self, key: str) -> None:
        """
        Executa o pressionamento de uma tecla do teclado.

        Args:
            key (str): Identificador da tecla (ex: 'enter', 'tab', 'esc').
        """
        pyautogui.press(key)

    def command_write(self, text: str) -> None:
        """
        Simula a digitação de uma sequência de caracteres.

        Args:
            text (str): Conteúdo textual a ser inserido no elemento em foco.
        """
        pyautogui.write(text)

    def command_click(self, target: Union[tuple, str]) -> None:
        """
        Executa um evento de clique do botão esquerdo do mouse.

        Args:
            target (Union[tuple, str]): Coordenadas cartesianas (x, y) ou
                caminho do arquivo de imagem para localização via OCR/Template Matching.
        """
        pyautogui.click(target)

    def command_hotkey(self, keys: List[str]) -> None:
        """
        Executa uma combinação de teclas de atalho (simultâneas).

        Args:
            keys (List[str]): Lista de strings representando as teclas (ex: ['ctrl', 'v']).
        """
        pyautogui.hotkey(*keys)

    def command_scroll(self, clicks: int) -> None:
        """
        Executa a rolagem (scroll) vertical na interface.

        Args:
            clicks (int): Quantidade de unidades de rolagem. Valores positivos
                rolam para cima, valores negativos rolam para baixo.
        """
        pyautogui.scroll(clicks)
