"""kant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kant.views import test1, test2, cuestionarioC, corporal, cognitivo, ambos
from cuestionario.views import quest, quest2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basurero/', test1, name="pruebas"),
    path('', test2, name="lobby"),
    path('cuestionario/', quest, name="cuestionario"),
    path("cuestionario2/", quest2, name="cuestionario2"),
    path("cuestionarioC/", cuestionarioC, name="cuestionarioC"),
    path("cuestionarioC/cognitivo", cognitivo, name="cognitivo"),
    path("cuestionarioC/corporal", corporal, name="corporal"),
    path("cuestionarioC/ambos", ambos, name="ambos")
]
