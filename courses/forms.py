from django.contrib.gis import forms
from DG_API.utils.widgets import CoordinatesWidget
from .models import Hole


class HoleForm(forms.ModelForm):
    class Meta:
        model = Hole
        fields = '__all__'
        widgets = {
            'center': CoordinatesWidget(),
            'tee_box': CoordinatesWidget(),
            'basket': CoordinatesWidget(),
        }
