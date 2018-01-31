from django.shortcuts import render, redirect, get_object_or_404,render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from tabla.forms import *


def inicio(request):
    listado = Elemento.objects.all()
    return render(request, "index.html",{"registros":listado})
