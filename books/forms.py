from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'genre',
            'reading_status',
            'rating',
            'cover_url',
            'cover_image',
            'aesthetic_tag',
            'publication_year',
            'pages',
            'language',
            'isbn',
            'description',
            'favorite_quote',
            'is_featured',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control aesthetic-input',
                'placeholder': 'e.g., The Secret History'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control aesthetic-input',
                'placeholder': 'e.g., Donna Tartt'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-select aesthetic-input'
            }),
            'reading_status': forms.Select(attrs={
                'class': 'form-select aesthetic-input'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-select aesthetic-input'
            }),
            'cover_url': forms.URLInput(attrs={
                'class': 'form-control aesthetic-input',
                'placeholder': 'https://images.unsplash.com/... or leave blank if uploading file'
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'form-control aesthetic-input'
            }),
            'aesthetic_tag': forms.TextInput(attrs={
                'class': 'form-control aesthetic-input',
                'placeholder': 'e.g., Dark Academia, Autumn Mood, Timeless'
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control aesthetic-input',
                'placeholder': 'e.g., 1992'
            }),
            'pages': forms.NumberInput(attrs={
                'class': 'form-control aesthetic-input',
                'placeholder': 'e.g., 559'
            }),
            'language': forms.TextInput(attrs={
                'class': 'form-control aesthetic-input',
                'placeholder': 'e.g., English'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control aesthetic-input',
                'placeholder': 'e.g., 978-1400031702'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control aesthetic-input',
                'rows': 4,
                'placeholder': 'Reflect upon the essence, mood, or storyline of this tome...'
            }),
            'favorite_quote': forms.Textarea(attrs={
                'class': 'form-control aesthetic-input',
                'rows': 3,
                'placeholder': '“Beauty is terror. Whatever we call beautiful, we quiver before it.”'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input aesthetic-checkbox'
            }),
        }


class AestheticRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control aesthetic-input',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control aesthetic-input',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control aesthetic-input',
            'placeholder': 'name@sanctuary.com'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control aesthetic-input',
            'placeholder': 'Choose a unique username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control aesthetic-input',
            'placeholder': 'Create a secure passphrase'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control aesthetic-input',
            'placeholder': 'Confirm your passphrase'
        })


class AestheticLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control aesthetic-input',
            'placeholder': 'Username or email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control aesthetic-input',
            'placeholder': 'Enter your passphrase'
        })

