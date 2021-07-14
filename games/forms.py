from django.contrib.gis import forms
from DG_API.utils.widgets import CoordinatesWidget
from .models import Stroke


class StrokeForm(forms.ModelForm):
    class Meta:
        model = Stroke
        fields = '__all__'
        widgets = {
            'position': CoordinatesWidget(),
        }
