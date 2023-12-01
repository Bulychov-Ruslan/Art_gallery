from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import *
from .models import *


def detail(request, pk):
    global comment_form
    item = get_object_or_404(Item, pk=pk)
    comments = Comment.objects.filter(item=item, reply=None).order_by('id')
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]

# Проверка лайка
    is_liked = False
    if item.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)

            comment = Comment.objects.create(item=item, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return redirect('item:detail', pk=item.id)
    else:
        comment_form = CommentForm()

    context = {
        'item': item,
        'related_items': related_items,
        'is_liked': is_liked,
        'total_likes': item.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'item/detail.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = NewItemForm()
    return render(request, 'item/form.html', {'form': form})


def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)
    return render(request, 'item/form.html', {'form': form, 'title': 'Edit item'})


def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')


def like_item(request):
    item = get_object_or_404(Item, id=request.POST.get('item_id'))
    is_liked = False
    if item.likes.filter(id=request.user.id).exists():
        item.likes.remove(request.user)
        is_liked = False
    else:
        item.likes.add(request.user)
        is_liked = True
    return redirect('item:detail', pk=item.id)


