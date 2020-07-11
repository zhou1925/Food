from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, UserForm, UserEditForm, AddMealForm, EditMealForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Meal, Driver, Customer, Order


def signup(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST, request.FILES)

        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))
            return redirect('food:dashboard')
    else:
        user_form = UserForm()
        restaurant_form = RestaurantForm()

    return render(request,'registration/signup.html',
                         {'user_form': user_form,
                         'restaurant_form': restaurant_form})

@login_required
def edit_account2(request):
    user_form = UserEditForm(instance=request.user)
    restaurant_form = RestaurantForm(instance=request.user.restaurant)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        restaurant_form = RestaurantForm(request.POST, request.FILES, instance=request.user.restaurant)

    return render(request, 'food/edit_account.html', {'user_form':user_form,
                                                    'restaurant_form':restaurant_form})


def dashboard(request):
    meals = Meal.objects.filter(restaurant=request.user.restaurant).order_by("-id")

    return render(request, 'food/dashboard.html', {'meals':meals})


@login_required
def restaurant_meal(request):
    meals = Meal.objects.filter(restaurant=request.user.restaurant).order_by("created")
    return render(request, 'food/meal.html', {'meals':meals})
    

@login_required
def restaurant_order(request):

    if request.method == 'POST':
        order = Order.objects.get(id=request.POST["id"], restaurant=request.user.restaurant)
        #order = get_object_or_404(Order, id=request.POST["id"], restaurant=request.user.restaurant)
        print(order)
        if order.status == 'progress':
            order.status = 'ready'
            order.save()
        
    orders = Order.objects.filter(restaurant= request.user.restaurant).order_by('-created')
    
    return render(request, 'food/order.html', {'orders':orders})


@login_required
def restaurant_report(request):
    return render(request, 'food/report.html')


@login_required
def add_meal(request):
    form = AddMealForm()

    if request.method == 'POST':
        form = AddMealForm(request.POST, request.FILES)

        if form.is_valid():
            meal = form.save(commit=False)
            meal.restaurant = request.user.restaurant
            meal.save()
            return redirect('food:restaurant-meal')

    return render(request, 'food/add_meal.html', {'form': form})

def edit_meal(request, meal_id):
    form = EditMealForm(instance=Meal.objects.get(id=meal_id))

    if request.method == 'POST':
        form = EditMealForm(request.POST, request.FILES,
        instance=Meal.objects.get(id=meal_id))
        if form.is_valid():
            form.save()
            return redirect('food:restaurant-meal')

    return render(request, 'food/edit_meal.html', {'form':form})