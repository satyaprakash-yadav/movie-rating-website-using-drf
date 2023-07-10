from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Movie
import os
import kaggle
from django.conf import settings
from MovieProject import settings
import zipfile

# Create your views here.

def home(request):
    return render(request, "MovieApp/home.html")



# - Register

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect('login')
        
    context = {'form': form}
    
    return render(request, 'MovieApp/register.html', context=context)


# - Login a user

def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                messages.success(request, "You have logged!")

                return redirect("dashboard")
    
    context = {'form': form}

    return render(request, 'MovieApp/login.html', context=context)



@login_required(login_url="login")
def dashboard(request):
    my_records = Movie.objects.all()
    data = ""
    for row in my_records:
        data = f"{row.status}"
    context = {'records': my_records, "status": data}
    return render(request, 'MovieApp/dashboard.html', context=context)



@login_required(login_url="login")
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")
        
    context = {"form": form}

    return render(request, "MovieApp/create-record.html", context=context)



@login_required(login_url="login")
def movie_detail(request, id):
    my_records = Movie.objects.filter(id=id)
    view = my_records.values()[0]['views_count']
    view += 1
    Movie.objects.filter(id=id).update(views_count=view)
    context = {'records': my_records}
    return render(request, "MovieApp/movie-detail.html", context=context)


# - Update a Record

@login_required(login_url="login")
def update_record(request, pk):

    record = Movie.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == "POST":

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {"form": form}

    return render(request, "MovieApp/update-record.html", context=context)




# - Delete a record

@login_required(login_url="login")
def delete_record(request, pk):

    record = Movie.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")



# Download dataset from kaggle api

# def moviedata(request):
#     # Authenticate with kaggle API
#     kaggle.api.authenticate(username = settings.KAGGLE_USERNAME, key = settings.KAGGLE_KEY)
#     kaggle.api.dataset_download_files('movies_metadata.csv', path=r'C:\Users\SUPER-COMPUTERS\Desktop\movie-rental-application\MovieProject', unzip=True)

def download_dataset(request):
    # Your dataset URL on kaggle
    dataset_url = "https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv"

    # Set the destination directory where you want to download the dataset
    destination_dir = os.path.join(settings.BASE_DIR, "datasets")

    # Download the dataset using the kaggle API
    kaggle.api.competition_download_files(dataset_url, path=destination_dir, unzip = True)

    return HttpResponse("Dataset download successfully.")




# - User Logout

def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout successfully!")
    return redirect("login")

