from django.shortcuts import render

from .forms import ProfileForm

# Create your views here.
def index(request):
    """A view to return the home page"""

    form = ProfileForm()

    context = {
        'form': form
    }

    return render(request, "home/index.html", context)