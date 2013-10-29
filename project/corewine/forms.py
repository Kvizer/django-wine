import json
from django.forms import (
    ModelForm,
    ValidationError,
    CharField,
    TextInput,
    Textarea,
    RadioSelect
)
from .models import (
    Wine,
    Region,
    Appelation,
    Producer,
    Country,
    Tag,
    Cepage,
)
class WineForm(ModelForm):

    class Meta:
        model = Wine

        fields = (
            'wineType','region', 'name','producer','year','country','alcool','appelation',\
            'date', 'code_saq', 'price', 'mouth_intensity', 'nose_intensity',\
            'rating', 'teint', 'aroma', 'taste', 'acidity', 'tanin', 'persistance', 'cepage', 'tag'
        )
        # On va commencer pour overrider seulement region pour voir si ca fonctionne
        widgets = {
            'region': TextInput(),
            'appelation': TextInput(),
            # 'country': TextInput(),
            'producer': TextInput(),
            'wineType': RadioSelect(),
            # 'cepage' : TextInput(),
            # 'tag': TextInput(),
        }

    
    