from django.shortcuts import render
from django.http import HttpResponse
from home.models import todo_data
from django.shortcuts import redirect

# Create your views here.
def home(request):
    if request.method == "POST":
        data= request.POST

        title = data.get("title" , "undefined")
        desc = data.get("desc" , "undefined")

        todo_data.objects.create(
            title = title ,
            desc = desc
        )

        return redirect("/")

    else:
        # return HttpResponse("this is our home page ")
        data = todo_data.objects.all()
        context = {
            "data" :data
        }
        return render(request , "index.html" , context)
    

def delete(request , title):
    print(title)

    data = todo_data.objects.get(title = title)
    data.delete()

    return redirect("/")

def update(request , title):

    if request.method == "POST":
        data = request.POST
        title2 = data.get("title")
        desc = data.get("desc")

        result = todo_data.objects.get(title=title)
        result.title = title2
        result.desc = desc
        result.save()
        
        return redirect("/")

    else:
        print(title)

        data = todo_data.objects.get(title = title)
        context = {
            "title" : data.title,
            "desc" :data.desc
        }
        return render(request , "update.html" , context)