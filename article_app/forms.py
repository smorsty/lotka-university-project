from django import forms


class FullSearch(forms.Form):
    keyword = forms.CharField(label='Kлючевое слово', required=False)
    authors = forms.CharField(label='Автор', required=False)
    start_year = forms.IntegerField(label='от', required=False, initial=1996)
    end_year = forms.IntegerField(label='до', required=False, initial=2022)


class CategoryFilterForm(forms.Form):
    CATEGORY_CHOICES = [
        ['Foundations', 'Foundations'],
        ['Secret-key cryptography', 'Secret-key cryptography'],
        ['Cryptographic protocols', 'Cryptographic protocols'],
        ['Public-key cryptography', 'Public-key cryptography'],
        ['Applications', 'Applications'],
        ['Implementation', 'Implementation'],
        ['Attacks and cryptanalysis', 'Attacks and cryptanalysis'],
        ['Uncategorized', 'Uncategorized'],
    ]

    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=CATEGORY_CHOICES,
        required=False
    )
