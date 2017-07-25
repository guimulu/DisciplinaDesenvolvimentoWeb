# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post
from .models import Comentario
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts_publicados = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, "post_list.html", {'posts': posts_publicados})

def coment_list(request):
    post = Post.objects.get(id=pk)
    comentarios = Comentario.objects.filter(post=post)

    return render(request, 'coment_list.html', {'post': post, 'comentarios': comentarios})