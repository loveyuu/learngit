# encoding=utf-8
from django.forms import ModelForm, CharField
from pagedown.widgets import AdminPagedownWidget

from .models import Blog


class BlogForm(ModelForm):
    content = CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Blog
        fields = '__all__'
        # widgets = {
        #     'title': Input(attrs={'class': "form-control", 'placeholder': u"文章标题"}),
        #     'content': Textarea(attrs={'class': "form-control",
        #                                'placeholder': u"文章内容",
        #                                'rows': 20
        #                                }),
        # }
