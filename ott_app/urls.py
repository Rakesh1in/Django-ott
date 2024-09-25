

# custom code start
#---------------------

from django.contrib import admin
from django.urls import path


from ott_app.views import fun_index,fun_view,fun_update,fun_delete,fun_search

urlpatterns = [
    path("", fun_index, name="home"),
    path("view/<int:primarykey>",fun_view,name="view_movie"),
    path("update/<int:primarykey>",fun_update,name="update_movie"),
    path("delete/<int:primarykey>",fun_delete,name="delete_movie"),
    path("search/",fun_search,name="search_movie"),
    
]

#---------------------
# custom code end