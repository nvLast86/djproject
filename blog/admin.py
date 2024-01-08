from django.contrib import admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'create_date', 'is_published', 'count_view')
    search_fields = ('title', 'text', 'create_date', 'is_published', 'count_view')
    list_filter = ('title', 'create_date', 'is_published', 'count_view')

