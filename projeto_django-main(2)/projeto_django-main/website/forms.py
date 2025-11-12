from django import forms
from funcionario.models import Funcionarios

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        # Define os campos que estarão no formulário
        fields = ['nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao']

        # Opcional: Adiciona classes Bootstrap para estilização
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 000.000.000-00'}),
            'tempo_de_servico': forms.NumberInput(attrs={'class': 'form-control'}),
            'remuneracao': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }