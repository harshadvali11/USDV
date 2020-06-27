from django import forms
from django.core.exceptions import ValidationError

def check_for_a(s):
    if s[0].lower()!='a':
        raise forms.ValidationError('name should start with a')

def check_for_even(n):
    if n%2!=0:
        raise ValidationError('number is not even')


class ContactForm(forms.Form):
    name=forms.CharField(max_length=15,required=True,validators=[check_for_a])
    number=forms.IntegerField(max_value=50,required=True,validators=[check_for_even])
    botcatcher=forms.CharField(max_length=20,widget=forms.HiddenInput,required=False)
    Email=forms.EmailField(max_length=50)
    Re_Enter_Email=forms.EmailField(max_length=50)


    def clean_botcatcher(self):
        bot=self.cleaned_data.get('botcatcher')
        if len(bot)>0:
            raise ValidationError('data is not entered bu human')

    
    def clean(self):
        e=self.cleaned_data.get('Email')
        r=self.cleaned_data.get('Re_Enter_Email')

        if e!=r and e!=re:
            raise forms.ValidationError('emails not matched')












