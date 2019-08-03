from django.urls import path

from . import views
# wire views into polls/urls

urlpatterns = [
		# url: /polls/
    path('', views.index, name='index'),
]