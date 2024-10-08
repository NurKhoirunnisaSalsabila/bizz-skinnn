from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "skin_type"]
    # ["name", "price", "description", "skin_type", "stock", "rating"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_skin_type(self):
        skin_type = self.cleaned_data["skin_type"]
        return strip_tags(skin_type)