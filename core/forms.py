from django import forms


class TestEmailForm(forms.Form):
    name = forms.CharField(label="FullName", max_length=50, required=True)
    subject = forms.CharField( max_length=50, required=True)
    email = forms.EmailField( required=True)
    message= forms.CharField( max_length=250, required=True, widget=forms.widgets.Textarea())