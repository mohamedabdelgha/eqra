from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'



















# # from django.forms import ModelForm
# # from .models import Member
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms


# # class Orderform(ModelForm):
# #     class meta:
# #         model = Member
# #         fields = '__all__'

# class CreateUserForm(UserCreationForm):
#     class meta:
#         model = User 
#         field = ['username', 'email', 'password1','password2']  
