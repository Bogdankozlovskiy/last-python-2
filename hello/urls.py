from django.urls import path
from hello import views


urlpatterns = [
    path('world/', views.hello)
]
