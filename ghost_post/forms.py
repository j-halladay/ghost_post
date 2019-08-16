from django import forms


class AddMessage(forms.Form):
    text = forms.CharField(max_length=280)
    is_boast = forms.BooleanField(required=False)
