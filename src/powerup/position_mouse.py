"""
Módulo utilitário para mapeamento de coordenadas de interface.

Este módulo fornece ferramentas para identificar a posição exata do cursor 
no monitor, facilitando a calibração de scripts de RPA.
"""

import pyautogui


class PositionMouse:
    """
    Classe utilitária para gerenciamento e captura de coordenadas do mouse.

    Fornece métodos para extrair a posição atual do cursor, essencial para
    mapear os campos de preenchimento do sistema alvo.
    """

    def get_position_mouse(self) -> pyautogui.Point:
        """
        Captura e exibe a posição atual do cursor no console.

        Returns:
            pyautogui.Point: Objeto contendo as coordenadas cartesianas (x, y).
        """
        current_position = pyautogui.position()
        print(f"Coordenadas capturadas: {current_position}")
        return current_position