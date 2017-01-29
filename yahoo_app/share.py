from urllib.request import urlopen
from datetime import datetime
from bs4 import BeautifulSoup

class Share():
	"""Classe ação"""

	def __init__(self, symbol=""):
		"""Inicializa a ação com o seu símbolo"""

		self.symbol = symbol

	def __str__(self):

		return "Ação: " + self.name + "\nCotação: " + self.quote + "\nHorário da última atualização: " + self.update_time + "\nPreço de compra: " + self.bid + "\nP/E (ttm): " + self.pe + "\nInformação obtida em: " + str(self.date)

	def get_share_information(self):
		"""Obtém as informações da ação do site da yahoo finanças"""

		try:
			html = urlopen("https://br.financas.yahoo.com/q?s=" + self.symbol)
			bsObj = BeautifulSoup(html)
		except:
			print("Erro ao acessar o yahoo para a ação: " + self.symbol)

		print("Obtendo informações da ação: " + self.symbol)

		try:
			self.date = datetime.now()
			self.name = bsObj.find("div", {"class": "title"}).find("h2").string
			self.update_time = bsObj.find("span", {"id": "yfs_t53_" + self.symbol.lower()}).string
			self.quote = bsObj.find("span", {"id": "yfs_l84_" + self.symbol.lower()}).string
			share_table = bsObj.find_all("td", {"class": "yfnc_tabledata1"})
			self.bid = share_table[2].string
			self.pe = share_table[12].string
		except:
			print("Erro ao obter informações da página")