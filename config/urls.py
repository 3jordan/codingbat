"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import warmup_one_view, warmup_two_view, cat_dog_view, logic_two_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-1/near-hundred/<int:number>", warmup_one_view),
    path("warmup-2/string-splosion/<str:word>", warmup_two_view),
    path("string-2/cat-dog/<str:string>", cat_dog_view),
    path("logic-2/lone-sum/<int:numberA>/<int:numberB>/<int:numberC>/", logic_two_view),
]
