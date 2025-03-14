from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['marca', 'model', 'an', 'kilometri', 'pret', 'tip_caroserie', 'putere_motor', 'capacitate_motor',
                  'descriere', 'imagine']

        widgets = {
            'descriere': forms.Textarea(attrs={'rows': 5}),
        }
