from django import forms
from .models import email_model
from tinymce import TinyMCE


def is_balance(test):
    xyz=test.split(",")
    #print(User.Profile.wallet)
    if(len(xyz)>1):
        return True
    else:
        return False

class mail_sender(forms.ModelForm):
    class Meta:
        model=email_model
        fields=['recipients','subject','body','user']
    recipients=forms.CharField(max_length=1000,
    label="",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
               
                "placeholder":'Recipients'
            }
        ))
        
    user=forms.CharField(max_length=500,
    label="Username",
            widget=forms.TextInput(
            attrs={
                "class":"form-inline",
                
                "placeholder":'User'
            }
            )
    
    )

    subject=forms.CharField(max_length=200,
    label="",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                
                "placeholder":'Subject'
            }
        ))

    body=forms.CharField(max_length=2000,

        label="",
        widget=TinyMCE(attrs={

            "class":"form-control",
            
            "placeholder":'Write you Body Message here!'
            },
            mce_attrs={'width': "100%"})
        )



    # def clean_recipients(self):
    #     test=self.cleaned_data.get('recipients')
    #     user_name=self.cleaned_data.get('user')
    #     print(self.instance.user)
    #     print(user_name)
    #     if(is_balance(test)):
    #         #print("error")
    #         msg_txt='''Your Recipients count exceeds your Wallet Balance by {}.
    #         Please recharge or Reduce No of recipitents.
    #         '''.format("1")
    #         raise forms.ValidationError(msg_txt)
    #     print("Goes Below ")
    #     return test





   