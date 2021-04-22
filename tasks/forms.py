from django.forms import ModelForm
from .models import Post

class createform(ModelForm):
	class Meta:
		model=Post
		fields='__all__'

