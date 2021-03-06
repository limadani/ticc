from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'login$', views.login),
	url(r'logout$', views.logout),
	url(r'sobre$',views.about),
	url(r'torneios$', views.tournaments),
	url(r'resultados$', views.list_results),
	url(r'cadastrar$', views.signup),
	url(r'meu-cadastro$',views.update_participant_info),
	url(r'validar/(?P<participant_school>[a-zA-Z0-9_]*)$',views.validate_participants),
	
	url(r'groups',views.edit_group),
	url(r'(?P<tournament_id>[0-9]+)/(?P<competition_id>[0-9]+)$/groups', views.edit_group),

	url(r'equipes/$', views.teams),
	url(r'equipes/nova$', views.add_team),
	url(r'equipes/filtro_participantes$',views.participant_filter,name=' '),
	url(r'equipes/(?P<team_id>[0-9]+)$',views.edit_team),	
	
	url(r'torneios/novo', views.add_tournament),
	url(r'torneios/(?P<tournament_id>[0-9]+)$', views.tournament_details),
	url(r'torneios/editar/(?P<tournament_id>[0-9]+)$', views.edit_tournament),
	url(r'torneios/excluir/(?P<tournament_id>[0-9]+)$', views.remove_tournament),

	url(r'competicoes/novo/(?P<tournament_id>[0-9]+)$', views.add_competition),
	url(r'competicoes/(?P<competition_id>[0-9]+)$', views.competition_details),
	
	url(r'jogos/(?P<match_id>[0-9]+)$', views.match_details),
	url(r'jogos/novo/(?P<competition_id>[0-9]+)$', views.add_match),
	url(r'jogos/editar/(?P<match_id>[0-9]+)$', views.edit_match),
	url(r'jogos/excluir/(?P<match_id>[0-9]+)$', views.remove_match),
	url(r'jogos/(?P<match_id>[0-9]+)/gerenciar-equipes$', views.manage_teams),
	url(r'jogos/(?P<match_id>[0-9]+)/finalizar$', views.finish_match),
	url(r'jogos/sair/(?P<match_id>[0-9]+)$', views.leave_match),
	url(r'jogos/(?P<match_id>[0-9]+)/pontuar$', views.update_score),

	url(r'minhas-partidas$', views.my_matches),
]
