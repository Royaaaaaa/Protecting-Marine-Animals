from django.shortcuts import render

from django.http import *

from .models import *

import json

def index(request):
    return render(request, 'app01/index2.html')

def marinefamily(request):
    typelist= Type.objects.all()
    context={'typelist': typelist}
    return render(request,'app01/marinefamily.html',context)

def marinelife(request,id):
    type = Type.objects.get(pk=id)
    animalList = type.animal_set.all()
    # context={'animalList':animalList}
    context={'animalList':animalList,'typeid':type.id}
    return render(request, 'app01/marinelife.html', context)

def quiz(request):
    return render(request, 'app01/quiz.html')

def game(request):
    return render(request, 'app01/game.html')
def pickingrubbish(request):
    return render(request, 'app01/pickingrubbish.html')

def aboutUs(request):
    return render(request, 'app01/aboutUs.html')
def storyAndFact(request):
    return render(request,'app01/storyAndFact.html')
def puzzle(request):
    return render(request,'app01/puzzle.html')

# def search(request):
#     typelist = Type.objects.all()
#     colorlist = Color.objects.all()
#     sizelist = Size.objects.all()
#     context={"typeList":typelist,"colorList":colorlist,"sizeList":sizelist}
#     return render(request,'app01/search2.html',context)

def searchtype(req):
    type_id = req.GET.get('type')
    size_id = req.GET.get('size')

    type = Type.objects.get(pk=type_id)
    life_list = type.animal_set.all()
    life_dic = {}
    for animal in life_list:
        life_dic[animal.id] = animal.aName
    life_dic = json.dumps(life_dic)
    return HttpResponse(life_dic)

# def searchColor(req):
#     color_id = req.GET.get('color')
#     color = Color.objects.get(pk=color_id)
#     life_list = color.animal_set.all()
#     life_dic = {}
#     for animal in life_list:
#         life_dic[animal.id] = animal.aName
#     life_dic = json.dumps(life_dic)
#     return HttpResponse(life_dic)

def advsearch(req,*args,**kwargs):
    ##kwargs拿到的是{'type_id': '0', 'colour_id': '0', 'size_id': '0'},用户搜索输入
    input_list = {}
    condition = {}

    for k,v in kwargs.items():
        input_list[k] = int(v)
        if int(v):  ###如果输入为0，则取所有,便可以忽略这个条件
            condition[k] = int(v)
    print('前端数据是：', input_list)
    print('条件是',condition)
    type_list = Type.objects.all()
    colour_list = Color.objects.all()
    size_list = Size.objects.all()
    animal_list = Animal.objects.filter(**condition)
    context = {'input_list':input_list,"animal_list":animal_list,'type_list':type_list,'colour_list':colour_list,'size_list':size_list}
    return render(req,'app01/search2.html',context)


def showDetail(request,id):
    animal = Animal.objects.get(pk=id)
    locationList = animal.location_set.all()
    imagelist=animal.image_set.all()
    list = []
    list1 = []
    for location in locationList:
        lat = location.latAnimal
        lon = location.lonAnimal
        s=(lat,lon)
        list.append(s)
    for image in imagelist:
        list1.append(image.iName)
    context={'locationList':list}
    x = json.dumps(context)
    # context={'animal': animal,'locationList':list,'imagelist':list1}
    return render(request,'app01/showDetail.html',locals())
