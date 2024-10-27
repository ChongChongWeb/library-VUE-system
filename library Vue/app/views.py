import os.path
import time

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app.models import BookTypes, BookInfos
from server.settings import BASE_DIR


# Create your views here.

def toWelcomeView(request):

    return render(request, 'welcome.html')

def toTypeView(request):

    pageIndex = request.GET.get('pageIndex', 1)
    pageSize = request.GET.get('pageSize', 2)

    data = BookTypes.objects.all()

    page = Paginator(data, pageSize)

    resl = []

    for item in list(page.page(pageIndex)):

        resl.append({
            'id': item.id,
            'name': item.name
        })

    return render(request, 'types/data.html',
                  {'pageIndex': int(pageIndex), 'pageSize': int(pageSize), 'data': resl,
                            'count': page.count, 'pageTotal': page.page(pageIndex).paginator.num_pages})

def toTypeAddView(request):

    return  render(request, 'types/add.html')

def typeAddForm(request):

    BookTypes.objects.create(
        name=request.POST.get('name')
    )

    return redirect('/types/page/view')

def toTypeUpdView(request):

    info=BookTypes.objects.get(pk=request.GET.get('id'))

    return  render(request, 'types/upd.html', {'info': info})

def typeUpdForm(request):

    BookTypes.objects.filter(id=request.POST.get('id')).update(
        name=request.POST.get('name')
    )

    return redirect('/types/page/view')

def typeDelForm(request):

    BookTypes.objects.filter(id=request.GET.get('id')).delete()

    return redirect('/types/page/view')


def toInfoView(request):

    pageIndex = request.GET.get('pageIndex', 1)
    pageSize = request.GET.get('pageSize', 2)

    data = BookInfos.objects.all()

    page = Paginator(data, pageSize)

    resl = []

    for item in list(page.page(pageIndex)):

        resl.append({
            'id': item.id,
            'name': item.name,
            'img': item.img,
            'price': item.price,
            'intro': item.intro,
            'typeId': item.type.id,
            'typeName': item.type.name,
        })

    return render(request, 'infos/data.html',
                  {'pageIndex': int(pageIndex), 'pageSize': int(pageSize), 'data': resl,
                            'count': page.count, 'pageTotal': page.page(pageIndex).paginator.num_pages})

def toInfoAddView(request):

    types = BookTypes.objects.all()

    return  render(request, 'infos/add.html', {'types': types})

def InfoAddForm(request):

    image = request.FILES['img']

    # image.name = str(int(time.time()) * 1000) + '.' + image.name.split('.')[1]

    BookInfos.objects.create(
        name=request.POST.get('name'),
        price=request.POST.get('price'),
        intro=request.POST.get('intro'),
        type=BookTypes.objects.get(pk=request.POST.get('typeId')),
        img=uploaadImg(image)
    )

    return redirect('/infos/page/view')

def toInfoUpdView(request):

    types = BookTypes.objects.all()

    info = BookInfos.objects.get(pk=request.GET.get('id'))

    return  render(request, 'infos/upd.html', {'types': types, 'info': info})

def InfoUpdForm(request):

    image = request.FILES['img']

    # image.name = str(int(time.time()) * 1000) + '.' + image.name.split('.')[1]

    BookInfos.objects.filter(id=request.POST.get('id')).update(
        name=request.POST.get('name'),
        price=request.POST.get('price'),
        intro=request.POST.get('intro'),
        type=BookTypes.objects.get(pk=request.POST.get('typeId')),
        img=uploaadImg(image)
    )

    return redirect('/infos/page/view')

def InfoDelForm(request):

    BookInfos.objects.filter(id=request.GET.get('id')).delete()

    return redirect('/infos/page/view')

def uploaadImg(img):

    imgName = str(int(time.time()) * 1000) + '.' + img.name.split('.')[1]

    filePath = os.path.join(BASE_DIR, 'static', 'imgs', imgName)

    with open(filePath, 'wb+') as destination:
        for chunk in img.chunks():
            destination.write(chunk)

    return 'static/imgs/' + imgName