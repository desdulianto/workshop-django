from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    pilihan = forms.ChoiceField(label='Pilihan',
                    choices=(('hello', 'Hello'),
                             ('bye', 'Bye-bye')))
