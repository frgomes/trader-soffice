import requests

def send_form_data(url, data):
  """Sends form data to a specified URL using POST method.

  Args:
    url: The URL of the endpoint to send the data to.
    data: A dictionary containing the form data.

  Returns:
    The response from the server.
  """

  response = requests.post(url, data=data)
  return response

# Example usage:
url = "http://fundamentus.com.br/resultado.php"
form_data = {
	"pl_min": "",
	"pl_max": "",
	"pvp_min": "3",
	"pvp_max": "",
	"psr_min": "",
	"psr_max": "",
	"divy_min": "",
	"divy_max": "",
	"pativos_min": "",
	"pativos_max": "",
	"pcapgiro_min": "",
	"pcapgiro_max": "",
	"pebit_min": "",
	"pebit_max": "",
	"fgrah_min": "",
	"fgrah_max": "",
	"firma_ebit_min": "",
	"firma_ebit_max": "",
	"firma_ebitda_min": "",
	"firma_ebitda_max": "",
	"margemebit_min": "",
	"margemebit_max": "",
	"margemliq_min": "",
	"margemliq_max": "",
	"liqcorr_min": "",
	"liqcorr_max": "",
	"roic_min": "",
	"roic_max": "",
	"roe_min": "",
	"roe_max": "",
	"liq_min": "",
	"liq_max": "",
	"patrim_min": "",
	"patrim_max": "",
	"divbruta_min": "",
	"divbruta_max": "",
	"tx_cresc_rec_min": "",
	"tx_cresc_rec_max": "",
	"setor": "",
	"negociada": "ON",
	"ordem": "1",
	"x": "27",
	"y": "15"
}

response = send_form_data(url, form_data)
print(response.text)


"""

Header
---------------------------------------------------
Referer: https://fundamentus.com.br/buscaavancada.php
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0
---
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: en-GB,en;q=0.7,pt-BR;q=0.3
"""
