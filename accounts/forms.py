from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, PasswordResetForm
from django.utils.translation import gettext, gettext_lazy as _
User = get_user_model()

class RegisterForm(forms.ModelForm):
    """
    Registration form
    """

    password = forms.CharField(widget=forms.PasswordInput())
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'password', 'password_2']
    
    def cleaned_user(self):
        """
        Verify registration code exists.
        """
        user_name = self.cleaned_data.get('username')
        obj = User.objects.filter(username=user_name)
        
        if obj.exists():
            raise forms.ValidationError('Registration number exists')
        return user_name
    
    def clean(self):
        """
        Verify both passwords matched.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('pssword_2')

        if password is not None and password != password_2:
            self.add_error('password_2', 'Your password must match')
        
        return cleaned_data
    

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new admins users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserCreationForm(forms.ModelForm):
    """
    A form for creating new admins users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        
    )

    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName', 'password']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
