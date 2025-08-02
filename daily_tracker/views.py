from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
from .models import Leave, StandupRecord
import json

User = get_user_model()


@login_required
def tracker_view(request):
    """Daily tracker view"""
    context = {
        'user': request.user,
    }
    return render(request, 'daily_tracker/tracker.html', context)


@permission_required('daily_tracker.add_leave')
def record_daily_view(request):
    """View for recording leave and standup responses"""
    if request.method == 'POST':
        data = json.loads(request.body)
        date_str = data.get('date')
        leave_entries = data.get('leave_entries', [])
        standup_defaulter_usernames = data.get('standup_defaulters', [])
        
        # Parse date or use today
        if date_str:
            try:
                record_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                record_date = timezone.now().date()
        else:
            record_date = timezone.now().date()
        
        # Process leave entries
        leave_records = []
        for entry in leave_entries:
            username = entry.get('username')
            half = entry.get('half', 0)  # Default to 0 (Full Day)
            
            try:
                user = User.objects.get(username=username)
                leave_record = Leave(
                    user=user,
                    date=record_date,
                    half=half
                )
                leave_records.append(leave_record)
            except User.DoesNotExist:
                continue
        
        # Process standup entries
        standup_records = []
        all_users = User.objects.filter(is_active=True)
        
        # Create a set of usernames who are on leave (full day or first half) from current entries
        leave_usernames = set()
        for entry in leave_entries:
            username = entry.get('username')
            half = entry.get('half', 0)
            if half in [0, 1]:  # Full day or first half
                leave_usernames.add(username)
        
        # Also check existing leave records in database
        existing_leave_users = set(Leave.objects.filter(
            date=record_date,
            half__in=[0, 1]  # Full day or first half
        ).values_list('user__username', flat=True))
        
        # Combine both sets
        all_leave_usernames = leave_usernames.union(existing_leave_users)
        
        for user in all_users:
            # Check if user is on leave for full day or first half
            is_on_leave = user.username in all_leave_usernames
            
            # If user is not on leave and not in defaulters list, they responded
            responded = not is_on_leave and user.username not in standup_defaulter_usernames
            
            if not is_on_leave:  # Only create record if not on leave
                standup_record = StandupRecord(
                    user=user,
                    date=record_date,
                    responded=responded,
                    notes='' if responded else 'Did not respond to standup'
                )
                standup_records.append(standup_record)
        
        # Save all records
        Leave.objects.bulk_create(leave_records, ignore_conflicts=True)
        StandupRecord.objects.bulk_create(standup_records, ignore_conflicts=True)
        
        return JsonResponse({
            'success': True,
            'message': f'Successfully recorded {len(leave_records)} leave entries and {len(standup_records)} standup records for {record_date}'
        })
    
    context = {
        'today': timezone.now().date(),
    }
    return render(request, 'daily_tracker/record_daily.html', context)


def search_users(request):
    """AJAX endpoint for user search"""
    query = request.GET.get('q', '')
    if len(query) < 2:
        return JsonResponse({'users': []})
    
    users = User.objects.filter(
        username__icontains=query,
        is_active=True
    )[:10]  # Limit to 10 results
    
    user_list = [{'username': user.username, 'full_name': user.get_full_name() or user.username} for user in users]
    return JsonResponse({'users': user_list})
