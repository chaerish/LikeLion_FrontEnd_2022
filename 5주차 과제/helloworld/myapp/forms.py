from django import forms
from .models import GuessNumber

class PostForm(forms.ModelForm):
    class Meta:
        model=GuessNumber #어떤 모델을 사용할것이냐. 
        field=('num_lotto') #어떤 필드를 입력받을것이냐 
