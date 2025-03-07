from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Food, Consume, HealthGoal
from .forms import HealthGoalForm, FoodForm

@login_required
def index(request):
    """Display available food items & consumed food."""
    if request.method == "POST":
        food_consumed_name = request.POST['food_consumed']
        food_item = Food.objects.get(name=food_consumed_name)
        Consume.objects.create(user=request.user, food_consumed=food_item)

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, "app/index.html", {'foods': foods, 'consumed_food': consumed_food})

@login_required
def delete_consume(request, id):
    """Allow user to delete a consumed food item."""
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect("index")
    return render(request, "app/delete.html")

@login_required
def chart_data(request):
    """Returns JSON data for Chart.js visualization."""
    consumed = Consume.objects.filter(user=request.user)
    goal, _ = HealthGoal.objects.get_or_create(user=request.user)

    data = {
        "labels": [c.food_consumed.name for c in consumed],
        "carbs": [c.food_consumed.carbs for c in consumed],
        "proteins": [c.food_consumed.proteins for c in consumed],
        "fats": [c.food_consumed.fats for c in consumed],
        "calories": [c.food_consumed.calories for c in consumed],
        "goal_carbs": goal.carb_goal,
        "goal_proteins": goal.protein_goal,
        "goal_fats": goal.fat_goal,
        "goal_calories": goal.daily_calorie_goal,
    }

    return JsonResponse(data)

@login_required
def update_goals(request):
    """Allow users to set nutrition goals."""
    goal, _ = HealthGoal.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = HealthGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = HealthGoalForm(instance=goal)

    return render(request, "app/update_goals.html", {"form": form})

@login_required
def add_food(request):
    """Allow users to add new food items to the global database."""
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = FoodForm()
    return render(request, "app/add_food.html", {"form": form})

def register(request):
    """User registration view."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "app/register.html", {"form": form})
