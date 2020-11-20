from django import forms 
from .models import Feedback ,MarketPost



class MarketCreate(forms.ModelForm):
    class Meta:
        models = MarketPost
        fields = ['type_of_item','description','contact','image']
  
# creating a form 
class FeedbackForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Feedback 
  
        # specify fields to be used 
        fields = [ 
            "name", 
            "message", 
        ] 