from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin 


admin.site.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    summermote_fields = ('content')
# Register your models here.