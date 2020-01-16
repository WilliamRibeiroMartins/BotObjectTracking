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

        for stage in object_status:
            places.append(stage.text.strip())

        return places

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # Definindo como o parâmetro será passado
    code_group = parser.add_mutually_exclusive_group()
    code_group.add_argument('-c', '--code', action='append', dest='code',
                           default=[], help='Add object code to process. Each one have to be passed after the argument.')

    # Interpretando os argumentos passados como parâmetros
    args = parser.parse_args()
    codes = args.code

    track = Tracking()

    # Realizando o rastreamento de cada objeto
    for code in codes:
        print('==============================================')
        print('==============================================')

        print(f'Rastreando o pacote: {code}')

        places = track.track(code)

        for place in places:
            print(place)
            print('==============================================')

