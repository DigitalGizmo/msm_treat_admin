from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    change_form_template = 'journal/admin/journal_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'entry_date', 'ordinal', 
            'lat', 'lon', 'zoom_level', 'is_flippable', 'entry_text',
            'interpret_blurb', 'interpret_more']}),
        # ('Behind the scenes',   {'fields': ['status_num', 'edited_by', 
        #     'edit_date', 'notes']}),
    ]
    list_display = ('title', 'slug', 'entry_date', 'lat', 'lon', 'zoom_level')
    # list_filter     = ['status_num'] 
    # search_fields = ['title', 'slug']

    # def truncated_map_blurb(self, obj):
    #     return obj.map_blurb[:30] + "..."

admin.site.register(Entry, EntryAdmin)
