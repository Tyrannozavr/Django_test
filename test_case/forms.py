from django import forms


class Current_value(forms.Form):
    current = forms.DecimalField(max_digits=50, decimal_places=6)
    sts = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2)))
