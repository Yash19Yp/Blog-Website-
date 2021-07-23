from django.contrib import admin
from .models import Post, Exam, BlogComment, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    class Media:
        js = ('tinyinject.js',)

admin.site.register(Post, PostAdmin)
admin.site.register(Exam)
admin.site.register(BlogComment)
admin.site.register(Contact)
