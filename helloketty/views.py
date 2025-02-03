
from django.db import connection
from django.shortcuts import render 
from django.http import JsonResponse
from django.contrib.auth.models import User

def my_view(request):
    u = User.objects.get(id=1)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()
    data = {
        "rows" : rows ,
        "user" : u.id
    }
    return JsonResponse(data , safe=False)