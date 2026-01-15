"""
Módulo de gerenciamento de dados para o projeto PowerUp.

Este módulo é responsável por carregar e processar os dados externos (CSV)
que serão utilizados pelo bot de RPA para o preenchimento automático do sistema.
"""

import pandas as pd


class DataSet:
    """
    Gerencia a ingestão e o processamento de bases de dados.

    Esta classe abstrai as operações de leitura de arquivos utilizando a 
    biblioteca Pandas, garantindo que os dados estejam em um formato 
    iterável para o script de automação.
    """

    def read_dataset(self, file_path: str) -> pd.DataFrame:
        """
        Realiza a leitura de um arquivo CSV e o converte em um DataFrame.

        Args:
            file_path (str): Caminho relativo ou absoluto para o arquivo .csv.

        Returns:
            pd.DataFrame: Objeto contendo os dados estruturados da tabela.

        Raises:
            FileNotFoundError: Caso o caminho especificado não seja encontrado.
        """
        try:
            database = pd.read_csv(file_path)
            return database
        except FileNotFoundError as error:
            print(f"Erro: O arquivo no caminho '{file_path}' não foi encontrado.")
            raise error