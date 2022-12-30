from django import forms
#from tinymce.widget import TinyMCE

from . import models

class PhotoForm(forms.ModelForm):

    class Meta:
        model = models.Photo
        fields = ['image','caption']

class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Blog
       # content = forms.CharField(widget=TinyMCE(attrs={'cols':80,'rows':30}))
        fields = ['title','content']

class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)