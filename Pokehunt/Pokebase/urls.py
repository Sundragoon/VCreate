from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect

from . import views
from Pokehunt import settings

def logout_required(view):
    def f(request, *args, **kwargs):
        if request.user.is_anonymous():
            return view(request, *args, **kwargs)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return f

app_name = "Pokebase"
urlpatterns = [
    url(r'^$', logout_required(views.index), name='index'),
    url(r'^login/$', logout_required(auth_views.login), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'), 
    url(r'^register/$', logout_required(views.register), name='register'), 
    url(r'^home/$', views.home, name='home'),
    url(r'^trainer/(?P<trainer_id>[0-9]+)/$', views.trainerinfo, name='trainerinfo'),
    url(r'^pokemon/(?P<pokemon_id>[0-9]+)/$', views.pokemoninfo, name='pokemoninfo'),
]
