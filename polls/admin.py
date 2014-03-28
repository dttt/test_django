from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question of the poll', {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    # Add sort by pub_date
    list_filter = ['pub_date']
    # Search fields
    search_fields = ['question']

# Add poll to admin page
admin.site.register(Poll, PollAdmin)
# Add Choice to admin page
admin.site.register(Choice)
