from django import forms

class One(forms.Form):
    Title = forms.CharField(label='Заголовок:', widget=forms.TextInput())
    Url = forms.CharField(label='URL:', widget=forms.URLInput())
    TextArea = forms.CharField(label='Контент:', widget=forms.Textarea())
    CheckBox = forms.CharField(label='Публикация', widget=forms.CheckboxInput())

    NAMES_CHOICES = [(1, 'One'), (2, 'two')]

    Selection = forms.ChoiceField(choices=NAMES_CHOICES, label='Категории')
