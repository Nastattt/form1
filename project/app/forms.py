from django import forms


class UserForm(forms.Form):
    # ch = ((1,"Python")(2,"JavaScript"))
    name = forms.CharField(max_length=20, min_length=2)
    age = forms.IntegerField()
    # agree = forms.BooleanField(label = "Согласен на обработку персональных данных")
    # photo = forms.ImageField(required= False)
    # file = forms.FileField()
    # date = forms.DateTimeField()
    # launguages = forms.MultipleChoiceField(choices=ch)
    comment = forms.CharField(widget=forms.Textarea, label="комментарий")


class NewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='Название', widget=forms.TextInput(attrs={'class': 'main__input'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'main__textarea'}))
    is_published = forms.BooleanField(label="Опубликовано", initial=True)
    category = forms.ChoiceField(choices=((1, 'Cпорт'), (2, 'Красота')), label='Категория')


class CreateForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    building = forms.CharField()
    apartment = forms.IntegerField()
