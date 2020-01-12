#
#
#
#
#
from django import forms
from .models import Kakeibo

class KakeiboForm(forms.ModelForm):
    """
    New data registration
    """

    class Meta:
        model = Kakeibo
        fields = ['date', 'category', 'money', 'memo']