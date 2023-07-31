from django.forms import *
from .models import journal,Signature

class FormInputJournal(ModelForm):
    class Meta:
        model = journal
        fields = "__all__"
        widgets = {
                    'npp':NumberInput(attrs={'class': 'form-control'}),
                    'dateInput': TextInput(attrs={'class': 'form-control','type': 'date','format':'%d.%m.%Y'}),
                    'content': TextInput(attrs={'class': "form-control"}),
                    'executor': TextInput(attrs={'class': "form-control"}),
                    'datePeredachi': TextInput(attrs={'class': "form-control",'type': 'date','format':'%d.%m.%Y'}),
                    'controlPeriod': TextInput(attrs={'class': "form-control",'type': 'date','format':'%d.%m.%Y'}),
                    'painting': TextInput(attrs={'class': "form-control"}),
                    'mark': TextInput(attrs={'class': "form-control"}),
        }
class FormSignature(ModelForm):
    class Meta:
        model = Signature
        fields = "__all__"
        widgets = {
            'numberInput':TextInput(attrs={'class': 'form-control'}),
            'user':TextInput(attrs={'class': 'form-control'}),
            'nomenklatura':TextInput(attrs={'class': 'form-control'}),
        }
