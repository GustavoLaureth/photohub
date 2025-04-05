from django import forms
from django.forms import ModelForm
from .models import Cliente, Tag

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['tags'].required = True  # ← obrigatório!

        # Remove a classe "form-control" de 'tags' (para não quebrar layout)
        self.fields['tags'].widget.attrs.pop('class', None)