from django import forms
from .models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["reason", "visit_date"]
        visit_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
