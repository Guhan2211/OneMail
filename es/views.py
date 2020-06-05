from django.shortcuts import render,redirect,get_object_or_404
from .forms import mail_sender as ms
from .mail import m_wtout_attach as mwa
from django.contrib.auth.models import User
from django import forms
from .models import email_model as em
from django.contrib.auth.decorators import login_required




@login_required(redirect_field_name='login',login_url="/")
def create(request):
    if request.method=="POST":
       
        form=ms(request.POST)
        
        if form.is_valid():
            
            instance = form.save(commit=False)
            instance.user=request.user.username
           

            rcvrs_str=form.cleaned_data['recipients']
            rcvrs=rcvrs_str.split(",")
            #request.user.profile.wallet
            if(len(rcvrs)>request.user.profile.wallet):
                temp=len(rcvrs)-request.user.profile.wallet
                err='''Your Recipients count exceeds your Wallet Balance by {}.
                Please recharge or Reduce No of recipitents.
                '''.format(temp)
                context={
                    "form":form,
                    "errors":err
                }
                return render(request,"es/form.html",context)
            else:
                sub=form.cleaned_data['subject']
                body=form.cleaned_data['body']
                instance.save()
                
                
                u = User.objects.get(id=request.user.id)
                u.profile.wallet=u.profile.wallet-len(rcvrs)
                u.save()
                mwa(rcvrs,sub,body)
                success="Your Mails are  Sent"

                print("Mails are sent rendering new template")
                es_form=ms(initial={"user":request.user.username})
                context={
                    "success":success,
                    "form":es_form

                    }
                return render(request,"es/form.html",context)
        else:
            context={"form":form}
            return render(request,"es/form.html",context)


    else:
       
        es_form=ms(initial={"user":request.user.username})
        context={
            "form":es_form
        }
        return render(request,"es/form.html",context)