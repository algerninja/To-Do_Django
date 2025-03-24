from django import forms


class RegisterForm(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "shift-input", "placeholder": "Nombre"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "shift-input", "placeholder": "Apellido"}
        )
    )

    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "shift-input", "placeholder": "Usuario"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"class": "shift-input", "placeholder": "Correo"}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "shift-input", "placeholder": "Contraseña"}
        ),
        required=True,
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "shift-input", "placeholder": "Confirmacion de Contraseña"}
        ),
        required=True,
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="",
        max_length=200,
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "shift-input", "placeholder": "Correo"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "shift-input", "placeholder": "Contraseña"}
        ),
        required=True,
    )
