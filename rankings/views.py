from django.shortcuts import render
from website.models import *
from collections import *

# Create your views here.

def statistics(request):
    matches = Match.objects.filter(finished=True)
    campis = Campus.objects.all()

    teams = [[],[],[]]

    medal_board = {}
    
    for match in matches:
        if match.competition.category.need_time:
            matchscore = MatchScore.objects.filter(match=match).order_by('-score','time')
            teams[0].append(matchscore[0].team)
            teams[1].append(matchscore[1].team)
            teams[2].append(matchscore[2].team)
        else:
            matchscore = MatchScore.objects.filter(match=match).order_by('-score')
            teams[0].append(matchscore[0].team)
            teams[1].append(matchscore[1].team)
            teams[2].append(matchscore[2].team)

    for campus in campis:
        medal_board[str(campus)] = 0

    for i in range(len(teams)):
        for team in teams[i]:
            if(team.mix_team==False):
                if(i==0):
                    medal_board[str(team.members.first().campus)] = medal_board [str(team.members.first().campus)] + 100
                elif(i==1):
                    medal_board[str(team.members.first().campus)] = medal_board [str(team.members.first().campus)] + 10
                else:
                    medal_board[str(team.members.first().campus)] = medal_board [str(team.members.first().campus)] + 1
            else:
                for participant in team.members.all():
                    if(i==0):
                        medal_board[str(participant.campus[i])] = medal_board[str(participant.campus[i])] + 100
                    elif(i==1):
                        medal_board[str(participant.campus[i])] = medal_board[str(participant.campus[i])] + 10
                    else:
                        medal_board[str(participant.campus[i])] = medal_board[str(participant.campus[i])] + 1


    medal_board = OrderedDict(sorted(medal_board.items(), key=lambda t: t[1], reverse=True))
    print(medal_board)

    campus_key = medal_board.keys()
    campus_values = medal_board.values()
    tuples = zip(campus_key, campus_values)

    context = {
        'title': 'Rankings e Estatísticas',
        'tuples': tuples,
        'campis': campis,

        'breadcrumb': [
            {'name': 'Início', 'link': '/'},
            {'name': 'Rankings'},
        ],
        "teste": 21
    }
    return render(request, 'rankings.html', context)