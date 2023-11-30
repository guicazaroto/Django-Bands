from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer

# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', { 'produtos': produtos })

def add(request):
    return render(request, 'add.html')

def save(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')

        Produto.objects.create(
            nome=nome,
            preco=preco,
            estoque=estoque
        )
        produtos = Produto.objects.all()

        return render(request, 'index.html', { 'produtos': produtos })

def edit(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'edit.html', { 'produto': produto })

def update(request, id):
    if request.method == 'POST':
        produto = Produto.objects.get(id=id)

        produto.nome = request.POST.get('nome')
        produto.preco = request.POST.get('preco')
        produto.estoque = request.POST.get('estoque')

        produto.save()

        return redirect(home)

def delete(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    
    return redirect(home)

class ApiProdutoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ApiProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer