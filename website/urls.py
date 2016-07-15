from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'torneios$', views.torneios),
	url(r'torneios/novo', views.torneios_novo),
	url(r'torneios/(?P<pk>[0-9]+)$', views.torneios_detalhes),
	url(r'torneios/editar/(?P<pk>[0-9]+)$', views.torneios_editar),
	url(r'torneios/excluir/(?P<pk>[0-9]+)$', views.torneios_excluir),

	url(r'competicoes/novo/(?P<pkTorneio>[0-9]+)$', views.competicoes_novo),
	url(r'competicoes/(?P<pkCompeticao>[0-9]+)$', views.competicoes_detalhes),
	url(r'competicoes/editar/(?P<pkCompeticao>[0-9]+)$', views.competicoes_editar),
	
	url(r'jogos/novo/(?P<pkCompeticao>[0-9]+)$', views.jogos_novo),
	url(r'jogos/(?P<pkJogo>[0-9]+)$', views.jogos_detalhes),
	url(r'jogos/editar/(?P<pkJogo>[0-9]+)$', views.jogos_editar),
]
