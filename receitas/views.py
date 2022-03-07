from django.shortcuts import render


# Create your views here.
def index(request):

  receitas = {
    1: 'Sopa de Legumes',
    2: 'Sorvete',
    3: 'Lasanha',
    4: 'Bolo de Chocolate',
  }
  dados = {
    'nome_das_receitas': receitas
  }
  return render(request,'index.html', dados)

def receita(request):
  return render(request, 'receita.html')