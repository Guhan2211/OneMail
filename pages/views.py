from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import rf
from .pay import cli
from django.views.decorators.csrf import csrf_exempt
from .models import Profile as p
from .models import pay_hist as ph


def index(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def profile(request):
    if(request.method=='POST'):
        mails=request.POST['count']
        mails=int(mails)
        amt=int((mails/50)*10)
        
        
        obj=get_object_or_404(p,id=request.user.id)
        obj.temp_mail=mails
        obj.temp_amnt=amt
        obj.save()
        

        
        DATA = {
            "amount":amt*100,
            "currency":"INR",
            "receipt":"order_rcptid_01",
            "notes":{'Info':'You are paying to oneMail'},
            "payment_capture":'0'
        }
                
        #print(DATA)
        response=cli.client.order.create(DATA)
        o_id=response['id']
        o_stat=response['status']

        if o_stat=='created':
            context={
                'Amount':amt,
                'Mail':mails,
                'Name':request.user.username,
                'Email':request.user.email,
                'order_id':o_id
            }

            return render(request,'confirm_order.html',context)





        form_inp=rf()
        context={"form":form_inp}
        return render(request,'profile.html',context)
    form_inp=rf()

    hist=ph.objects.filter(user=request.user.username)

    

    context={"form":form_inp,"hist":hist}
    return render(request,'profile.html',context)


def payment_status(request):
    response=request.POST
    #print(response)
    params_dict={
        'rpid':response['razorpay_payment_id'],
        'roid':response['razorpay_order_id'],
        'rs':response['razorpay_signature']
    }
    try:
        obj=get_object_or_404(p,id=request.user.id)
        
        mails=obj.temp_mail
        amt=obj.temp_amnt
        

        
        cli.client.payment.capture(response['razorpay_payment_id'],amt*100 , {"currency":"INR"})
        
        print("captured")
    except Exception as e:
        print(str(e))
        print("not captured")
        pass
    
    try:
        cli.client.utility.verify_payment_signature(params_dict)
        
        obj=get_object_or_404(p,id=request.user.id)
        
        obj.temp_mail=0
        obj.temp_amnt=0
        obj.save()
        print("payment Failure")
        return redirect('profile')  

  
    except Exception as e:
        obj=get_object_or_404(p,id=request.user.id)
        p_obj=ph(
            user=request.user.username,
            order_id=response['razorpay_order_id'],
            pay_id=response['razorpay_payment_id'],
            amnt=obj.temp_amnt
            )
        
        p_obj.save()
        obj.wallet=obj.wallet+obj.temp_mail
        obj.temp_mail=0
        obj.temp_amnt=0
        obj.save()

        print(str(e))
        print("success")
        return redirect('profile')
    