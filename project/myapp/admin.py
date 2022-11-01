from django.contrib import admin
from myapp.models import *

# Register your models here.

class WidgetAdmin(admin.ModelAdmin):
    list_display = ['id','name','font_size','price','quantity','total_price']
admin.site.register(Widget, WidgetAdmin)

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','city')
admin.site.register(MyUser,MyUserAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','tagline')
admin.site.register(Blog,BlogAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
admin.site.register(Author,AuthorAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('id','blog','headline','body_text','pub_date','mod_date','number_of_comments',
    'number_of_pingbacks','rating','get_authors')
admin.site.register(Entry,EntryAdmin)

class DogAdmin(admin.ModelAdmin):
    list_display = ('id','name','data')
admin.site.register(Dog,DogAdmin)
