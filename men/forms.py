from django import forms
from .models import *


class AddArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category not selected'

    class Meta:
        model = Men
        fields = ['name', 'last_name', 'content', 'photo', 'slug', 'year_of_birth',
                  'year_of_death', 'age', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
