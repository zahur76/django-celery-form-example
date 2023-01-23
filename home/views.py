from django.shortcuts import render, redirect, reverse
import time
from .tasks import debug_task

from .forms import ProfileForm

# Create your views here.
def index(request):
    """A view to return the home page"""

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        data = form.data
        if form.is_valid():
            print('doda')
            debug_task.delay(data)
            print('form submitted')
            return redirect(reverse("home"))
        else:
            print(form.errors)
            return redirect(reverse("home"))

    form = ProfileForm()

    context = {
        'form': form
    }

    return render(request, "home/index.html", context)