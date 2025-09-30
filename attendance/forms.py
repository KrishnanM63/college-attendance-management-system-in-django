from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class register_form(forms.ModelForm):
    username = forms.CharField(label="username",max_length=100,required=True)
    roll_num = forms.CharField(label="roll_num",max_length=100,required=True)
    email = forms.CharField(label="email", max_length=100, required=True)
    password = forms.CharField(label="password",max_length=100,required=True)
    confirm_password= forms.CharField(label="confirm_password",max_length=100,required=True)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def clean(self):
        cleand_data = super().clean()
        
        password = cleand_data.get("password")
        confirm_password = cleand_data.get("confirm_password")  
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("passwords are mismatched")  
        
class login_frm(forms.Form):
    login_as = forms.ChoiceField(
        choices=[("admin", "Admin"), ("student", "Student")],
        label="Login as"
    )
    username = forms.CharField(label="name",max_length=100,required=True)
    password = forms.CharField(label="password",max_length=100,required=True)
    
    def clean(self):
        clean_data= super().clean()
        username = clean_data.get('username')
        password = clean_data.get('password')
        
        if username and password:
            user = authenticate(username = username , password = password)
            if user is None:
                raise forms.ValidationError("username and password is incorrect!")
        
    
            
        