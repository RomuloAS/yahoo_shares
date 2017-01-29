from yahoo_app.share import Share
from yahoo_app.file_io import read_shares_list, write_csv


def shares_io():
	"""Busca as informações e grava em um arquivo csv"""

	print("Lendo lista de ações")
	shares_list = read_shares_list("lista_acoes.txt")
	shares = []

	print("Obtendo informações")
	for s in shares_list:
		share = Share(s)
		share.get_share_information()
		shares.append(share)

	print("Iniciando gravação do arquivo")
	write_csv("shares_table.csv", shares)
	print("Gravação completa")

	return shares