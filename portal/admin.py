from django.contrib import admin 
from portal.models import main_page  
# Patient Article Admin
class main_page_Admin(admin.ModelAdmin):
    fieldsets = [
    ('Title', {'fields':['title', 'encode',  'div_id']}),
    ]
admin.site.register(main_page, main_page_Admin)

#--------------------------------------------------------

