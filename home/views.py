from django.shortcuts import render, redirect, reverse
import time

from .forms import ProfileForm

# Create your views here.
def index(request):
    """A view to return the home page"""

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            print('form submitted')
            return redirect(reverse("home"))
        else:
            print('form invalid')
            return redirect(reverse("home"))

    form = ProfileForm()

    context = {
        'form': form
    }

    return render(request, "home/index.html", context)