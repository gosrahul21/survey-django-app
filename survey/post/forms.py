from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['gender','age','income','education']
        widgets = {
            'gender': forms.RadioSelect(attrs={"required": "required"}),
            'age':forms.RadioSelect(attrs={"required": "required"}),
            'income':forms.RadioSelect(attrs={"required": "required"}),
            'education':forms.RadioSelect(attrs={"required": "required"}),
            }   
