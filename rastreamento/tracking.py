import argparse
import requests

from bs4 import BeautifulSoup

class Tracking():
    base_url = 'https://rastro.ideris.com.br/Correio.aspx?objeto='

    def track(self, object_id: str):
        """
        Realiza o rastreamento do objeto
        """
        places = list()
        # Define a url do objeto a ser rastreado
        object_url = self.base_url + object_id

        # Interpretando a página
        response = requests.get(object_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscando todos os locais pelo qual o objeto passou
        object_status = soup.find_all('tr')

        if not object_status:
            return None
        
        for stage in object_status:
            places.append(stage.text.strip())

        return places

