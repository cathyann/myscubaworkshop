from django.shortcuts import render

# Create your views here.


def coming_soon(request):
    """A view to return the leisure & courses page """
    
    return render(request, 'coming_soon/coming_soon.html')