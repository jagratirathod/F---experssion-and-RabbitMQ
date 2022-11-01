from tkinter import N
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import F 
from django.db.models import ExpressionWrapper, DecimalField
from django.db.models import Sum


# Create your views here.

def hello(request):
    # wid=Widget.objects.update(total_price=F('price')*F('quantity'))
    # wid=Widget.objects.all().annotate(
    # value_in_stock=ExpressionWrapper(
    #     F('price') * F('quantity'), output_field=DecimalField()
    #     )
    # )
    
    # wid=Widget.objects.aggregate(total_price=Sum(F("price")*F('quantity')))
    
    # wid=Widget.objects.filter(price__gte=F(40))
    
    
    # wid=Widget.objects.filter(id=2).update(total_price=F('price')*F('quantity'))
    # print(wid.first().total_price)

    ent=Entry.objects.select_related().all()
    print(ent)
    for x in ent:
        print(x)
    return HttpResponse('hii')

