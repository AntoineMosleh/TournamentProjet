import itertools
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tournament,Match
from .forms import TournamentForm, ParticipantForm

def home(request):
    form = TournamentForm()
    return render(request, 'home.html', {'form': form})

def home(request):
    tournaments = Tournament.objects.all()
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TournamentForm()
    print(tournaments)
    return render(request, 'home.html',context={'tournaments': tournaments, 'form': form})

def add_participant(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            tournament.participants.add(participant)
            return redirect('displayTournamentDetails', tournament_id=tournament_id)
    else:
        form = ParticipantForm()
    return render('displayTournamentDetails', tournament_id=tournament_id)

def create_match_for_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament,pk=tournament_id)
    participantsAuTournoi = list(tournament.participants.all())
    combinations = list(itertools.combinations(participantsAuTournoi, 2))
    for combination in combinations:
        Match.objects.create(
            tournament=tournament,
            firstParticipant=combination[0],
            secondParticipant=combination[1]
    )
    tournament.isStarted = True
    tournament.save()
    return redirect('displayTournamentDetails', tournament_id=tournament_id)
    
def addScoreForMatch(request, match_id,tournament_id):
    match = get_object_or_404(Match, pk=match_id)
    scoreFirstParticipant = int(request.POST.get('firstParticipantScore'))
    scoreSecondParticipant = int(request.POST.get('secondParticipantScore'))
    
    match.firstParticipantScore = scoreFirstParticipant
    match.secondParticipantScore = scoreSecondParticipant
    
    if scoreFirstParticipant > scoreSecondParticipant:
        match.winner = match.firstParticipant
        match.firstParticipant.points += 3
    elif scoreFirstParticipant < scoreSecondParticipant:
        match.winner = match.secondParticipant
        match.secondParticipant.points += 3
    else:
        match.firstParticipant.points += 1
        match.secondParticipant.points += 1
        
    match.save()
    match.firstParticipant.save()
    match.secondParticipant.save()

    return redirect('displayTournamentDetails', tournament_id=tournament_id)

def displayTournamentDetails(request, tournament_id):  
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    participants = tournament.participants.all().order_by('-points')
    participant_form = ParticipantForm()

    matches = Match.objects.filter(tournament=tournament).select_related('firstParticipant', 'secondParticipant')

    return render(request, 'tournament_detail.html', {
        'tournament': tournament,
        'participants': participants,
        'matches': matches,
        'participant_form': participant_form
    })
    
    
    
        
        
    
    