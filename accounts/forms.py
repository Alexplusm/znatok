from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.translation import ugettext_lazy as _
from .models import Profile


User = get_user_model()

DUPLICATE_EMAIL = _(u"Данный адрес электронной почты уже используется.")


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text=_(u'email address'),
        required=True,
    )

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(DUPLICATE_EMAIL)
        return self.cleaned_data['email']

    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    username = forms.CharField(label='Логин', disabled=True)
    email = forms.EmailField(disabled=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(format='%d.%m.%Y'),
                               help_text='Введите дату в формате дд.мм.гггг', required=False)#=forms.SelectDateWidget(years=range(1940, 2010)))
    city = forms.CharField(label='Город', required=False)
    user_avatar = forms.FileField(label='Изменить аватар', widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ('user_avatar', 'birthday', 'city',)


class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"), strip=False,
                                   widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=_("New password"), widget=forms.PasswordInput,
                                    strip=False, help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("New password confirmation"), strip=False,
                                    widget=forms.PasswordInput)
