from .models import CustomUser
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts




class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'myfieldclass'}),
                                help_text="<br>".join(password_validators_help_texts()))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    

    class Meta:
        model = CustomUser
        fields = ['username', 'email','name', 'gender','image']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        validate_password(password1)
        return password2

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user


class UserCreationFormAdmin(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'myfieldclass'}),
                                help_text="<br>".join(password_validators_help_texts()))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    

    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        validate_password(password1)
        return password2


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = CustomUser
        fields = ['email','name','gender','image']

    def clean_password(self):
        return self.initial["password"]


        
class UserChangeFormAdmin(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeFormAdmin
    add_form = UserCreationFormAdmin

    list_display = ('username', 'name',  'is_superuser','admin','id')
    list_filter = ( )

    fieldsets = (
        ('Login', {'fields': ('username', 'password')}),
        ('Profile', {'fields': ('name', 'email', 'gender','image', 'notifications', 'noti_messages')}),
        ('Permissions', {'fields': ( 'is_admin', 'admin' )}),
        
    )

    add_fieldsets = (
        ('Login', {'fields': ('username', 'password1', 'password2')}),
        ('Profile', {'fields': ('name', 'email', 'gender','image')}),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()
    

    def get_form(self, request, obj=None, **kwargs):
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        # if 'user_permissions' in form.base_fields:
        #     permissions = form.base_fields['user_permissions']
        #     permissions.queryset = permissions.queryset.exclude(
        #         content_type__app_label__in=['admin', 'auth', 'contenttypes', 'sessions', 'user_auth', 'authtoken'])
        return form


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)

