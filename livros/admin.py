from django.contrib import admin
from livros.models import Autor, Livro
from rangefilter.filter import DateRangeFilter
class AdminAutor(admin.ModelAdmin):
    list_display = ( 'nome',)
    list_filter = ( 'nome',)
    search_fields=['nome']
admin.site.register(Autor, AdminAutor)
class AdminLivro(admin.ModelAdmin):
    list_display = ('titulo', 'isbn', 'autor','data_pub')
    list_filter = ('titulo' ,('data_pub', DateRangeFilter),'categoria')
    search_fields=['titulo','autor__nome','data_pub']
admin.site.register(Livro, AdminLivro)
admin.site.site_header = 'My Project'
admin.site.index_title = 'My Project'
admin.site.site_title = 'My Project'