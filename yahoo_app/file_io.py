import csv
from yahoo_app.share import Share

def read_shares_list(name):
	"""Função para ler ações do arquivo txt informado"""

	try:
		with open(name) as file_object:
			shares = file_object.readlines()
			return [share.replace(';\n', '.SA').upper() for share in shares]
	except:
		print("Erro ao ler arquivo")


def write_csv(name, shares):
	"""Cria/Atualiza arquivo com as ações"""

	try:
		with open(name) as csvfile:
			create_header = False
	except:
		create_header = True
		print("Arquivo não existe")
		print("Criando Arquivo")

	with open(name, 'a') as csvfile:
		fieldnames = ['Ação', 'Cotação', 'Horário da última atualização', 'Preço de compra', 'P/E (ttm)', 'Informação obtida']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		if create_header:
			writer.writeheader()
		for s in shares:
			try:
				writer.writerow({'Ação': s.name,'Cotação': s.quote, 'Horário da última atualização': s.update_time, 'Preço de compra': s.bid, 'P/E (ttm)': s.pe, 'Informação obtida': str(s.date)})
			except:
				print("Erro ao escrever o arquivo")
				continue

def read_csv(name):
	"""Lê o arquivo com a ultima atualização das ações"""

	try:
		with open(name) as csvfile:
			reader = csv.reader(csvfile)
			reader = list(reader)[::-1]
			reader = reader[:11]
			reader = reader[::-1]

			shares = []
			for r in reader:
				share = Share()
				share.name = r[0]
				share.quote = r[1]
				share.update_time = r[2]
				share.bid = r[3]
				share.pe = r[4]
				share.date = r[5][:-7]
				shares.append(share)

			return shares		

	except:
		print("Erro ao ler arquivo")