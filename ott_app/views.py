from django.shortcuts import render,redirect

# Create your views here.


# custom code start 
#--------------------------------

from django.http import HttpResponse
from ott_app.models import ott_app
from ott_app.forms import ott_app_form
from django.core.paginator import Paginator



# index page structure block of code
def fun_index(request): # request for url
    #objects_list = ott_app.objects.all()  # whithout filter (select * from ott_app_ott_app)
    objects_list = ott_app.objects.filter(is_publish=True).order_by('-movie_release_date')  # here indicates (select * from ott_app_ott_app) where is_publish=True order by movie_release_date decceinding.


    # pagination
    var_paginator = Paginator(objects_list,4) # howmany records fetch for page
    page_number = request.GET.get('page') # page number request getting with a name ('page' ur choice name)
    try:
        objects_list_final = var_paginator.get_page(page_number) # if number exist

    except PageNotAnInteger:
        objects_list_final = var_paginator.get_page(1) # if number not exist

    except EmptyPage:
        objects_list_final = var_paginator.page(var_paginator.num_pages) # if number empty

    context = {'post' : objects_list_final,'template':"HOME"}  # here converts to (fields[database_table_columns]) and (records[database_table_rows]) for tetching data in jinja format.
    return render(request,'ott/index.html',context)
    #return HttpResponse("<h1>Hello, world.</h1>") # response for url (checking purpose)




# view page structure block of code
def fun_view(request,primarykey):
    object_record_list = ott_app.objects.get(id=primarykey) # indicates (select * from ott_app_ott_app where id=primarykey)
    context = {'post' : object_record_list,'template':"VIEW",}
    return render (request,'ott/view.html',context)



# update page structure block of code
def fun_update(request,primarykey):
    object_record_list = ott_app.objects.get(id=primarykey) # indicates (select * from ott_app_ott_app where id=primarykey)
    
    if request.method=='POST': # if form submitted tru post method
        form = ott_app_form(request.POST,request.FILES,instance=object_record_list)

        if form.is_valid(): # if all form values is TRUE like as given model
            form.save() # form data saves in database
            return redirect ('view_movie',primarykey) # page redirecting to named 'view_movie' url

    form = ott_app_form(instance=object_record_list) #injuct getting (record_list) values to form
    return render (request,'ott/update.html',{'form':form,'cancel':object_record_list,'template':"UPDATE"})



# delete
def fun_delete(request,primarykey):
    # temporary delete (method-1) 
    object_record_list = ott_app.objects.filter(id=primarykey).update(is_publish=False)
    return redirect ('home')

    # perminent delete 
    #object_record_list.delete()
    #return redirect ('home')

    # temporary delete (method-2) 
    # objects_list = MyModel.objects.filter(id=primarykey)
    # for obj in objects_list:
    #     obj.is_publish = False
    #     obj.save()

# search page structure block of code

def fun_search(request):
    if request.method == "GET":
        x = request.GET.get('search')
        if x:
            y = ott_app.objects.filter(movie_name__icontains=x) # (__icontains check pattern upper&lowercases, __contains check pattern exact case only)
            return render(request,'ott/search.html',{'post':y,'template':"SEARCH",})
        else:
            return render(request,'ott/search.html',{'template':"SEARCH",})



#----------------------------------
# custom code end