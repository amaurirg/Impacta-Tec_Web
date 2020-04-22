from django.urls import path
from contas.views import registrar

app_name = "contas"
urlpatterns = [
    path('registrar/', registrar, name='registrar')
]
