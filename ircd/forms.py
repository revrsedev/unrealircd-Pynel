from django import forms
from .models import IrcServer

class IrcServerForm(forms.ModelForm):
    rpc_password = forms.CharField(widget=forms.PasswordInput, help_text="Enter the RPC password")

    class Meta:
        model = IrcServer
        fields = ['name', 'rpc_url', 'port', 'rpc_user', 'rpc_password']
