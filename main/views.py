from django.shortcuts import render, redirect, reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import JsonResponse
from .forms import ProductForm
import json


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # products = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2306165534',
        'name': request.user.username,
        'class': 'PBP A',
        # 'products': products,
        'last_login': request.COOKIES.get('last_login', 'Tidak Tersedia'),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    # data = Product.objects.all()
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    # data = Product.objects.all()
    data = Product.objects.filter(user=request.user.id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    
    product = Product.objects.get(pk = id)

   
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
 
    product = Product.objects.get(pk = id)

    product.delete()

    return HttpResponseRedirect(reverse('main:show_main'))

# New function to add product by AJAX
@csrf_exempt
@require_POST
def create_product_ajax(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return JsonResponse({
            "message": "Product created successfully",
            "product": {
                "id": str(product.id),
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "skin_type": product.skin_type,                 
            }
        }, status=201)
        
    else:
        return JsonResponse({"errors": form.errors}, status=400)
 

@csrf_exempt
# @login_required
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validasi data
            if not all(key in data for key in ["name", "price", "description", "skin_type"]):
                return JsonResponse({
                    "status": "error",
                    "message": "Missing required fields"
                }, status=400)

            new_product = Product.objects.create(
                user = request.user,
                name = data["name"],
                price = int(data["price"]),
                description = data["description"],
                skin_type = data["skin_type"]
            )

            new_product.save()

            return JsonResponse({
                "status": "success",
                "message": "Product created successfully"
            }, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON format"
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)
    
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    }, status=405)