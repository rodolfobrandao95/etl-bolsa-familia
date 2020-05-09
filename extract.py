import json
import requests as r


def consume_api(year, month, state_code, city_code, save_path):
    uri = 'http://www.transparencia.gov.br/api-de-dados/bolsa-familia-por-municipio/?mesAno={}{}&codigoIbge={}{}&pagina=1'.format(
        year, month, state_code, city_code)
    response = r.get(uri)

    if response.status_code == 200:
        with open(save_path, mode='w', encoding='utf-8') as output:
            temp = json.loads(response.text)
            json.dump(temp, output, ensure_ascii=False)

    return response.status_code


# Main:
if __name__ == "__main__":
    consume_api('2019', '01', '28', '00308', 'JSON/data.json')
