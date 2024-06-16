from django.contrib import admin
from .models import IrcServer
from .forms import IrcServerForm

class IrcServerAdmin(admin.ModelAdmin):
    form = IrcServerForm
    list_display = ('name', 'port', 'rpc_url')
    fields = ('name', 'port', 'rpc_url', 'rpc_user', 'rpc_password')
    search_fields = ('name', 'address')

admin.site.register(IrcServer, IrcServerAdmin)
