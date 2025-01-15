from django.shortcuts import render


def index(request):
    data = {
       "title": "Главная страница",
       "values" : ['Some','Hello','123'],
       "obj" : {
           "car" : "BMW",
           "age" : 18,
           "hobby" : "Baseball"
       }
    }
    return render(request,'main/index.html',data) #по django мы уже находимся в папе templates

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request,'main/contacts.html')