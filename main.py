import requests
import json


def dollar_exchange_rate(date):
    date = date
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/" \
          f"CotacaoDolarDia(dataCotacao=@dataCotacao)?%40dataCotacao='{date}'"
    response = requests.get(url)
    json.loads(response.content)
    values = json.loads(response.content)['value']
    purchase_quote = values[0]['cotacaoCompra']
    sell_quote = values[0]['cotacaoVenda']
    date_time_quote = values[0]['dataHoraCotacao']
    formated_date = date.replace('-', '/')
    print(f"Cotação do Dólar em {formated_date}:\n\n"
          f"Compra: R$ {purchase_quote}\n"
          f"Venda: R$ {sell_quote}\n"
          f"Data da Cotação: {date_time_quote}")


date = '10-05-2010'
dollar_exchange_rate(date)

# Estudar functools
