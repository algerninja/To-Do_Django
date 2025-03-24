from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(
        label="",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"class": "input-custom"}),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "text-area-custom",
                "onkeyup": "textAreaAdjust(this)",
                "rows": "1",
                "cols": "65",
                "wrap": "hard",
            }
        ),
        required=False,
    )
    completed = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "inp-cbx"})
    )
