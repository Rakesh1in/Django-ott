
# this form for custom design for admin


# custom code start
#--------------------------


from django import forms #forms importing....
from .models import ott_app # models class_name importing....
from datetime import datetime #exact datetime importing....

class ott_app_form(forms.ModelForm): # ott_app_form is child class and forms(modul).ModelForm(parentclass)
    class Meta:

        # models class (medel name mandatory as variable)
        model = ott_app

        # which fields do you want to presenting.. (fields name mandatory as variable)
        fields = [  'movie_poster',
                    'movie_name',
                    'movie_category',
                    'movie_release_date',
                    'movie_language',
                    'movie_director',
                    'movie_actors',
                    'movie_trailer_link',
                    'movie_stream_link',
                    'movie_imbd_rating',
                    'movie_views',
                    'movie_description',
                    'is_publish',
                ]

        # widgets for response view & {'class' : 'form-control'} for validations!
        widgets = {
            'movie_poster' : forms.FileInput(attrs={'class': 'form-control'}),
            'movie_name'  : forms.TextInput(attrs={'class': 'form-control'}),
            'movie_category' : forms.TextInput(attrs={'class': 'form-control'}),
            'movie_release_date' : forms.NumberInput(attrs={'type': 'date','class': 'form-control'}),
            'movie_language' : forms.TextInput(attrs={'class': 'form-control'}),
            'movie_director' : forms.TextInput(attrs={'class': 'form-control'}),
            'movie_actors' : forms.TextInput(attrs={'class': 'form-control'}),
            'movie_trailer_link' : forms.URLInput(attrs={'class': 'form-control'}),
            'movie_stream_link' : forms.URLInput(attrs={'class': 'form-control'}),
            'movie_imbd_rating' : forms.TextInput(attrs={'class': 'form-control'}),
            'movie_views' : forms.NumberInput(attrs={'class': 'form-control'}),
            'movie_description' : forms.Textarea(attrs={'class': 'form-control'}),
            'is_publish' : forms.CheckboxInput(),
        }


#--------------------------
# custom code end

