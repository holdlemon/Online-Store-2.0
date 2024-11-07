from django.forms import ModelForm

from catalog.forms import StyleFormMixin
from .models import Blog


class BlogForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Blog
        exclude = ('view_counter',)
