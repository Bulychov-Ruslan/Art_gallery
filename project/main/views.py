from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from item.models import *
from .models import *
from .forms import SignupForm, UserForm, UserEditForm, ProfileEditForm, MyForm
from django.core.paginator import Paginator


def index(request):
    items = Item.objects.all()
    users = User.objects.select_related('profile').filter()[0:6]
    paginator = Paginator(items, 6)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items,
        'users': users
    }
    return render(request, 'main/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            profile = Profile.objects.create(user=user)
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'main/edit_profile.html', context)


def authors(request):
    users = User.objects.select_related('profile').all()
    context = {'users': users}
    return render(request, 'main/authors.html', context)


def author(request, id):
    user = get_object_or_404(User, id=id)
    items = Item.objects.filter(created_by=user)
    context = {'user': user, 'items': items}
    return render(request, 'main/author.html', context)


def contact(request):
    return render(request, 'main/contact.html')


def about(request):
    return render(request, 'main/about.html')

