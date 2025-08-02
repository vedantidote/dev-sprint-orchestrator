from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    """Home dashboard view"""
    context = {
        'user': request.user,
    }
    return render(request, 'home.html', context) 