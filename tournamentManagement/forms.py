from django import forms
from .models import Tournament, Participant

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'sport']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sport': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }