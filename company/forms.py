from django import forms
from .models import Company
import re

class RegisterCompanyForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField()
    cnpj = forms.CharField(
        widget=forms.TextInput(attrs={
            'onkeyup': 'mascaraCnpj(this)',
            'placeholder' : 'CNPJ',
            'maxlength': 18
        })
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'onkeyup': 'mascaraTelefone(this)',
            'placeholder' : 'TELEFONE',
            'maxlength': 15
        })
    )
    email = forms.EmailField()

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        # Remove qualquer coisa que não seja número
        phone = re.sub(r'\D', '', phone)

        if len(phone) > 11:
            raise forms.ValidationError("Número de telefone deve ter no máximo 11 dígitos.")

        return phone
    
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj', '')
        return re.sub(r'\D', '', cnpj)

    class Meta:
        model=Company
        fields = ['name', 'description', 'cnpj', 'phone', 'email']