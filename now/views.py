from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from .models import SpeedcubingResult
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SpeedcubingResult

@login_required
def timer(request):
    return render(request, 'speedcubing/timer.html')

def time(request):
    return render(request, 'speedcubing/time.html')

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import SpeedcubingResult
from django.urls import reverse

def save_time(request):
    if request.method == 'POST':

        time_in_seconds = request.POST.get('time_in_seconds')


        CustomUser = get_user_model()
        current_user = CustomUser.objects.get(username=request.user.username)

        SpeedcubingResult.objects.create(user=current_user, time_in_seconds=time_in_seconds)


        return HttpResponseRedirect(reverse('best_results'))



    return render(request, 'speedcubing/best_results.html')


@login_required
def best_results(request):
    user_results = SpeedcubingResult.objects.filter(user=request.user).order_by('time_in_seconds')
    return render(request, 'speedcubing/best_results.html', {'user_results': user_results})



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'speedcubing/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('timer')
    else:
        form = AuthenticationForm()
    return render(request, 'speedcubing/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('glav')

def algor(request):
        return render(request, 'algor.html')

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TimerResult


def glav(request):
    last_timer_id = request.session.get('last_timer_id')
    return render(request, 'glav.html', {'last_timer_id': last_timer_id})

def we(request):
        return render(request, 'we.html')

def up(request):
        return render(request, 'up.html')

from django.shortcuts import redirect, get_object_or_404
from .models import SpeedcubingResult

def delete_result(request, result_id):
    result = get_object_or_404(SpeedcubingResult, id=result_id)
    if request.method == 'POST':
        result.delete()
    return redirect('best_results')
