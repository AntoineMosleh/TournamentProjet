from django.urls import path
from .views import home, create_match_for_tournament, add_participant, addScoreForMatch, displayTournamentDetails

urlpatterns = [
    path('', home, name='home'),
    path('tournament/<int:tournament_id>/', create_match_for_tournament, name='create_match_for_tournament'),
    path('add_participant/<int:tournament_id>/', add_participant, name='add_participant'),
    path('add_existing_participant/<int:match_id>/<int:tournament_id>/', addScoreForMatch, name='addScoreForMatch'),
    path('create_matches/<int:tournament_id>/', displayTournamentDetails, name='displayTournamentDetails'),
]