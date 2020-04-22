from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_users,admin_only

# Create your views here.
from django.urls import reverse


def login(request):
    return render(request, 'login.html')
def register(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url') #
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
@login_required(login_url="/login/")
@allowed_users(allowed_roles=['Manager'])
# @admin_only
def success(request):
    return render(request, 'success/success.html')
# @unauthenticated_user
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('index'),)

    # from django import template
    # from django.contrib.auth.models import Group
    #
    # register = template.Library()
    #
    # @register.filter(name='has_group')
    # def has_group(user, group_name):
    #     group = Group.objects.get(name=group_name)
    #     return group in user.groups.all()
