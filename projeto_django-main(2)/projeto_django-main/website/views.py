from django.shortcuts import render, get_object_or_404, redirect
from funcionario.models import Funcionarios
from .forms import FuncionarioForm # Importa o formulário criado

# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def listar_funcionarios(request):
    funcionarios = Funcionarios.objetos.all()
    # Adicionando o nome do autor para o requisito do título (Exemplo: Funcionários de Welison)
    # ATENÇÃO: Substitua "Guilherme Frey" pelo seu nome conforme o requisito 5.
    contexto = {"funcionarios": funcionarios, "autor": "Guilherme Freires"} 
    return render(request, 'website/funcionarios.html', contexto)

def detalhes_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    contexto = {"funcionario": funcionario}
    return render(request, 'website/detalhesFuncionario.html', contexto)

def cadastrar_funcionario(request): # Assinatura da função corrigida (sem 'id')
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:listar') # Redireciona para a listagem
    else:
        form = FuncionarioForm()

    contexto = {"form": form, "operacao": "Cadastrar"}
    return render(request, 'website/funcionario_form.html', contexto) # Novo template

def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)

    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('website:detalhes', id=funcionario.id) # Redireciona para os detalhes
    else:
        form = FuncionarioForm(instance=funcionario) # Preenche o formulário com dados existentes

    contexto = {"form": form, "operacao": "Editar"}
    return render(request, 'website/funcionario_form.html', contexto) # Novo template


def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    # Exclusão imediata sem confirmação:
    funcionario.delete()
    return redirect('website:listar')

# O código comentado de 'excluir_funcionario' foi mantido como estava.
# def excluir_funcionario(request, id):
#     funcionario = get_object_or_404(Funcionarios, pk=id)
#     if request.method == "POST":
#         funcionario.delete()
#         return redirect('website:listar')  # ou o nome de rota que lista
#     contexto = {"funcionario": funcionario}
#     return render(request, 'website/confirmar_excluir.html', contexto)