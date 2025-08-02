from django.contrib import admin
from .models import Leave, StandupRecord


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'get_half_display', 'created_at')
    list_filter = ('date', 'half', 'created_at', 'user')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    date_hierarchy = 'date'
    ordering = ('-date', 'user__username')
    
    def get_half_display(self, obj):
        """Custom display for half field"""
        choices = {0: 'Full Day', 1: 'First Half', 2: 'Second Half'}
        return choices.get(obj.half, 'Unknown')
    get_half_display.short_description = 'Leave Type'
    
    # Explicitly exclude any automatic columns
    list_display_links = ('user', 'date')
    
    fieldsets = (
        ('Leave Information', {
            'fields': ('user', 'date', 'half')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StandupRecord)
class StandupRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'responded', 'get_notes_preview', 'created_at')
    list_filter = ('date', 'responded', 'created_at', 'user')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'notes')
    date_hierarchy = 'date'
    ordering = ('-date', 'user__username')
    
    fieldsets = (
        ('Standup Information', {
            'fields': ('user', 'date', 'responded', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def get_notes_preview(self, obj):
        """Return a preview of the notes field"""
        if obj.notes:
            return obj.notes[:50] + '...' if len(obj.notes) > 50 else obj.notes
        return 'No notes'
    get_notes_preview.short_description = 'Notes Preview'
