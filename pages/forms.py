from django import forms

class rf(forms.Form):
    count=forms.IntegerField(
        
        min_value=50,
        initial=50,
        label="",
        widget=forms.NumberInput(
            attrs={
                "class":"mt-4 mr-2",
                "step":"50",
                "id":"order",
                "placeholder":'50'
            }
        )
           
    
    )
   