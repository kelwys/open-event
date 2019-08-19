"""open_event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from open_event.evento.views import home, inscricao_individual, detail, inscricao_lote

urlpatterns = [
    url(r'^$', home, name='home'),
    path('inscricao/', inscricao_individual),
    path('inscricao/<int:pk>/', detail),
    path('admin/', admin.site.urls),
    path('admin/inscricao_lote/', inscricao_lote),
]
admin.site.site_title = "OpenEvent Admin Portal"
admin.site.index_title = "Seja bem vindo ao OpenEvent"
