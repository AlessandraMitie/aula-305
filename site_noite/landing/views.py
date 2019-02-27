from django.shortcuts import render

def mostrar_index(request):
    nome = 'Enrique'
    lista_compras = ['arroz', 'feijão', 'açaí']
    return render(request, 'index.html', {'item' : nome, 'lista' : lista_compras})