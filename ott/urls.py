"""
URL configuration for my_sample_apps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path , include



from django.conf import settings # custom import for static root
from django.conf.urls.static import static # custom import for static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ott_app.urls")), # here include 'ott_app' is app directory name and urls is custom created urls for app level mappings! [use : if the app copies for another project no need to write again urls! in case if you write navigation here! you should write agian urls in project!]
    path("xky4k/accounts/", include("accounts_app.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# it manages static/ files (html,css,js), midia/ files (images,videos)!
# we have to write static(settings......) & import
# we can take static-settings from [web address : django documentaion ( serch > image)]


