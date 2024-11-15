from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet, Visit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import VisitForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
        else:
            # If the form is invalid, render the same page with errors
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})


@login_required
def dashboard(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, "pets/dashboard.html", {"pets": pets})


@login_required
def add_pet(request):
    if request.method == "POST":
        name = request.POST["name"]
        species = request.POST["species"]
        breed = request.POST.get("breed", "")
        Pet.objects.create(owner=request.user, name=name, species=species, breed=breed)
        return redirect("dashboard")
    return render(request, "pets/add_pet.html")


@login_required
def add_visit(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.pet = pet  # Assign the pet to the visit
            visit.save()
            return redirect('pet_detail', pet_id=pet.id)  # Redirect after successful form submission
    else:
        form = VisitForm()
    return render(request, 'pets/add_visit.html', {'form': form, 'pet': pet})



def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    visits = pet.visit_set.all()
    return render(request, 'pets/pet_detail.html', {'pet': pet, 'visits': visits})