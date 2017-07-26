# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

from .models import Post, Comentario
from django.utils import timezone
from .forms import formComentario, formNewPost

# Create your views here.
def post_list(request):
    posts_publicados = Post.objects.order_by('data_publicacao')
    return render(request, "post_list.html", {'posts': posts_publicados})

def new_post(request):
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
        comentarios = Comentario.objects.filter(post=post).order_by('data')
        form = formComentario()

    return render(request, 'coment_list.html', {'post': post, 'comentarios': comentarios, 'form': form})