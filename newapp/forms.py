from django import forms
from .models import Income, Outcome

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['tanggal', 'jumlah', 'sumber', 'deskripsi']  # Field yang akan dimasukkan dalam form

class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['tanggal', 'jumlah', 'sumber', 'deskripsi']  # Field yang akan dimasukkan dalam form
