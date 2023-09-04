from typing import Any, Dict
from django import forms
from .models import AuctionListing, Bid, Category

# adding forms

class ListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add an empty option to the category field's choices
        self.fields['category'].empty_label = 'The default category is "Other"'
    
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')

        # if the category is None (not chosen), set it to 'Other'
        if category is None:
            cleaned_data['category'] = Category.objects.get(name='Other')

        return cleaned_data

    class Meta:
        model = AuctionListing
        fields = ["title", "description", "primary_price", "imageUrl", "is_active", "category"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'primary_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'imageUrl': forms.URLInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ["amount"]
        labels = {
            'amount': 'Enter your bid amount',
        }

        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }
