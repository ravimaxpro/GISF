from django import forms
from myapp.models import Product
from .myformcommonvalidations import SpecialCharCheck
from .models import Product2
class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'fieldRequired'}))  # deriving fieldRequired from base.css and setting properties to name field
    url = forms.URLField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

BIRTH_YEAR_CHOICE=['1980','1981','1982']
FAVOURITE_COLOR_CHOICES=[
    ('blue','Blue'),
    ('black','Black'),
    ('green','Green'),
]

class ChoiceForm(forms.Form):
    birth_year=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICE))
    favourite_color=forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVOURITE_COLOR_CHOICES,
    )

class ProductFormvalidateForm(forms.ModelForm):
    title=forms.CharField(label='Title:',widget=forms.TextInput(attrs={'placeholder':'your title'}))
    #email=forms.EmailField()
    description=forms.CharField(required=False,
                               widget=forms.Textarea(
                               attrs={'placeholder':'ypor description',
                                      'class':'fieldRequired',
                                      'id':'My new id for Textarea',
                                      'rows':20,
                                      'cols':120
                                      }

                                ))
    price=forms.DecimalField(initial=199.000)

    class Meta:
        model=Product
        fields=['title','description','price']

    def clean_title(self, *args, **kwargs):  # syntax for filed validate is clean_<fildName>
        title = self.cleaned_data.get("title")
        print('title validation :', title)
        if 'CFE1' == title:
            print('inside :', title)
            raise forms.ValidationError("title is not correct value", "101")
        if title in ["CFE", "ABC"]:
            raise forms.ValidationError("title is not correct value1", "102")
        elif SpecialCharCheck(title):
            raise forms.ValidationError("Title Shouldnot contains Special Charaacters ", "103")
        return title


class product_form(forms.ModelForm):

   description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={'placeholder': 'your description',
                                             'class': 'fieldRequired',
                                             'id': 'My new id for Textarea',
                                             'rows': 20,
                                             'cols': 120
                                             }

                                  ))
   class Meta:
        model=Product2
        fields='__all__'

   def clean_title(self, *args, **kwargs):  # syntax for filed validate is clean_<fildName>
        title = self.cleaned_data.get("title")
        print('title validation :', title)
        if 'CFE1' == title:
            print('inside :', title)
            raise forms.ValidationError("title is not correct value", "101")
        if title in ["CFE", "ABC"]:
            raise forms.ValidationError("title is not correct value1", "102")
        elif SpecialCharCheck(title):
            raise forms.ValidationError("Title Shouldnot contains Special Charaacters ", "103")
        return title





