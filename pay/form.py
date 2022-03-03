from dataclasses import field, fields
from crispy_forms.helper import FormHelper
from django import forms
from .models import payment_num
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class Payform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Payform, self).__init__(*args, **kwargs)
        self.fields['phone_num'].widget.attrs['style'] = "width:300px" 
        self.fields['phone_num'].widget.attrs ={'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number',}
        self.fields['phone_num'].widget.attrs['placeholder'] = 'Enter your Phone  Number'
       
    class Meta:
        model = payment_num
        labels = {
        "phone_num": ("Phone Number")
    }
  
        fields = ('phone_num',)
       # validators=[RegexValidater(r'[0-9]')]

        # Widgets = {
        #     'phone_num' : forms.NumberInput(
        # }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper
            self.helper.form_method = 'post'
            




# class payment(forms.Form):
#     phone_num = forms.CharField(max_length=10)
  