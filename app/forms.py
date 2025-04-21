from django import forms
from .models import Header, Line
from django.forms import inlineformset_factory

class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['title']

LineFormSet = inlineformset_factory(
    Header,
    Line,
    fields=('description',),
    extra=1,
    can_delete=True
)