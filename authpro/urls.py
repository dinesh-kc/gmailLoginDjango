
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
# from django.contrib.auth.views import logout

from django.shortcuts import render



def index(request):
    context = {
        'posts': [{'title':"Authenticated"}]
        if request.user.is_authenticated else []
    }

    return render(request, 'index.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('', include('social_django.urls', namespace='social')),
#   path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
#     name='logout'),
]
