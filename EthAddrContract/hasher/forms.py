from django import forms

class RetreiveHostAddr(forms.Form):
    #bound form is connected to a database
    hostForm = forms.CharField()
    addrForm = forms.CharField()

