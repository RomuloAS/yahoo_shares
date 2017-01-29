from django.shortcuts import render
from yahoo_app.file_io import read_csv

def index(request):
	"""A página inicial de yahoo shares"""

	shares = read_csv("shares_table.csv")
	context = {'shares': shares}

	return render(request, 'yahoo_app/index.html', context)
