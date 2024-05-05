from django.contrib import admin
from boards.models import Board, List, Card
# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display=('title','project', 'created_at')

class ListAdmin(admin.ModelAdmin):
    list_display=('title','board','created_at')   
admin.site.register(Board, BoardAdmin)
admin.site.register(List, ListAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'labels', 'list', 'is_open')
admin.site.register(Card, CardAdmin)
