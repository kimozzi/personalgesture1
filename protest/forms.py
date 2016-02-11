from django import forms
from protest.models import Protest


class ProtestForm(forms.ModelForm):
    #is_agree = forms.BooleanField(label='약관동의', error_messages = {'required' : '약관에 동의해야함'})
    class Meta:
        model = Protest
        fields = ('type_of', 'title', 'content', 'photo', 'video', 'place', 'date', 'number_of_people')
