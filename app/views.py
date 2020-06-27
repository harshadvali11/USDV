from django.shortcuts import render

# Create your views here.
from app import forms



def validate(request):
    form=forms.ContactForm()
    if request.method=='POST':
        form_data=forms.ContactForm(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data.get('name')
            number=form_data.cleaned_data.get('number')
            Email=form_data.cleaned_data.get('Email')
            Re_Enter_Email=form_data.cleaned_data.get('Re_Enter_Email')
            d={'name':name,'number':number,'Email':Email,'Re_Enter_Email':Re_Enter_Email}
            return render(request,'form_data.html',context=d)

    return render(request,'form.html',context={'form':form})