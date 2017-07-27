# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

from .models import Post, Comentario
from django.utils import timezone
from .forms import formComentario, formNewPost
from django.contrib.auth import login, authenticate


# Create your views here.
def post_list(request):
    if request.user.id is None:
        return  redirect(logar)

    posts_publicados = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao').reverse()
    return render(request, "post_list.html", {'posts': posts_publicados})

def new_post(request):
    if request.user.id is None:
        return  redirect(logar)
    formNew = formNewPost()
    if request.method == "POST":
        formNew = formNewPost(request.POST)
        if formNew.is_valid():
            novoPost = formNew.save(commit=False)
            novoPost.autor = request.user
            novoPost.data_criacao = timezone.now()
            novoPost.save()
            return  redirect(post_list)
    else:
        return render(request, "new_post.html", {'form': formNew})


def coment_list(request, pk):
    if request.user.id is None:
        return  redirect(logar)
    if request.method == "POST":
        form = formComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.data = timezone.now()
            comentario.post = Post.objects.get(id=pk)
            comentario.save()
            return redirect(coment_list, pk=pk)
    else:
        post = Post.objects.get(id=pk)
        post.visualizacoes += 1
        post.save()
        comentarios = Comentario.objects.filter(post=post).order_by('data').reverse()
        form = formComentario()

    return render(request, 'coment_list.html', {'post': post, 'comentarios': comentarios, 'form': form})

def logar(request):
    if request.user.id is not None:
        return  redirect(post_list)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(post_list)
    return render(request, 'login.html', {})