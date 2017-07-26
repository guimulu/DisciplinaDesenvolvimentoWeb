from django import forms
from .models import Post, Comentario

class formComentario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('texto', )

class formNewPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'texto', 'data_publicacao',)
        widgets = {
            'data_publicacao': forms.DateTimeInput(attrs={'class':'datetimepicker'}),
        }