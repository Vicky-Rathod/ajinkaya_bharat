from .models import City,DailyFeed,Clipping,DailySpecialAkola,DailySpecialBuldhana,PageOneClip,PageTwoClip,TopAdds,BottomAdds
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.forms import CloudinaryFileField
from django.forms import ModelForm
class SignUpForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class DailyFeedForm(forms.ModelForm):

    date = forms.DateField(
                widget=forms.DateInput(attrs={
            'class': 'input1',
            'id':'datepicker',
            'placeholder':'Date of Newspaper',
            'label':'Date'
        })
        , required=False)
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label='Select City')

    class Meta:
        model = DailyFeed
        fields = '__all__'


class RetrieveForm(forms.Form):
    retrive_date = forms.DateField(input_formats=['%Y-%m-%d'],
                                   widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'trips_month'}),
                                   initial=timezone.now().today().strftime(
                                                         '%Y-%m-%d'))
class DailySpecialFeedForm(forms.ModelForm):

    date = forms.DateField(
                widget=forms.DateInput(attrs={
            'class': 'input1',
            'id':'datepicker',
            'placeholder':'Date of Newspaper',
            'label':'Date'
        })
        , required=False)

    class Meta:
        model = DailySpecialAkola
        fields = '__all__'

class DailySpecialBuldhanaForm(forms.ModelForm):
    date = forms.DateField(
                widget=forms.DateInput(attrs={
            'class': 'input1',
            'id':'datepicker',
            'placeholder':'Date of Newspaper',
            'label':'Date'
        })
        , required=False)
    class Meta:
        model = DailySpecialBuldhana
        fields = '__all__'


class ClippingForm(forms.ModelForm):
    class Meta:
        model = Clipping
        fields = ('clipimage',)

class PageOneClipForm(forms.ModelForm):

    page_date = forms.DateField(
                widget=forms.DateInput(attrs={
            'class': 'input1',
            'id':'datepicker',
            'placeholder':'Date of Newspaper',
            'label':'Date'
        }), required=False)

    class Meta:
        model = PageOneClip
        fields = '__all__'
class PageTwoClipForm(forms.ModelForm):
    page_two_date = forms.DateField(
                widget=forms.DateInput(attrs={
            'class': 'input1',
            'id':'datepicker',
            'placeholder':'Date of Newspaper',
            'label':'Date'
        }), required=False)
    class Meta :
        model = PageTwoClip
        fields = '__all__'
class TopAddsForm(forms.ModelForm):
    add_date = forms.DateField(
                widget=forms.DateInput(attrs={
            'class': 'input1',
            'id':'datepicker',
            'placeholder':'Date of Newspaper',
            'label':'Date'
        }), required=False)
    class Meta :
        model = TopAdds
        fields = '__all__'
class BottomAddsForm(forms.ModelForm):
    bottom_add_date = forms.DateField(
                widget=forms.DateInput(attrs={
            'class': 'input1',
            'id':'datepicker',
            'placeholder':'Date of Newspaper',
            'label':'Date'
        }), required=False)
    class Meta :
        model = BottomAdds
        fields = '__all__'