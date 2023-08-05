from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from GamePage.models import Account
from django.db import IntegrityError

def GamePage(request):   
    user = request.user
    account = Account.objects.get(user=user)
    print("account",account)
    balance = account.Balance
    return render(request, "GamePage.html",{'balance':balance})
def profile(request):
    user = request.user
    account = Account.objects.get(user=user)
    acc_context = {
        'balance': account.Balance,
        'phonenumber': account.Phone_Number,
    }
    print(account.Phone_Number)
    print(account.Balance)
    return render(request,"profile.html",acc_context)
def editprofile(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        pnumber = request.POST["pnumber"]
        user = User.objects.filter(username=username).first()
        if user:
            user.email = email
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            account = Account.objects.filter(user=user).first()
            if account:
                account.Phone_Number = pnumber
                account.save()
            messages.success(request, "Profile updated")
            return redirect('profile')
        else:
            messages.error(request, "User does not exist")
            return redirect('profile')
    user=request.user
    account = Account.objects.get(user=user)
    acc_context = {
        'balance': account.Balance,
        'phonenumber': account.Phone_Number,
    }
    return render(request,"editprofile.html",acc_context)
def HomePage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)
        print("user",user)
        try:
                account = Account.objects.get(user=user)
                print("account",account)
                balance = account.Balance
                print("balance",balance)
        except Account.DoesNotExist:
                # Handle the case when the account does not exist
                # You can set a default balance or display an error message
            print("Yuck")
            balance = 790  # Set a default balance
            messages.warning(request, "Account does not exist. Please contact support.")
        if user is not None:
            login(request, user)
            return render(request,"GamePage.html",{'user':username,'balance':balance})
        else:
            messages.error(request, "Bad Creditionals !!")
            return redirect('HomePage')
    return render(request, "HomePage.html") 
def Logout(request):
    logout(request)
    return render(request, "HomePage.html")
def signup(request):
    if request.method == "POST":
        try:    
            username = request.POST["username"]
            password = request.POST["password"]
            email= request.POST["email"]
            firstname = request.POST["fname"]
            lastname = request.POST["lname"]
            pnumber = request.POST["pnumber"]
            user = User.objects.create_user(username=username, password=password,email=email, **{'last_name': lastname, 'first_name': firstname})
            account = Account.objects.create(user=user,Phone_Number=pnumber)
            user.save()
            messages.success(request, user.username+" created an account")
            return redirect('signupsuccess')
        except IntegrityError:
                return redirect('signupfailure')
    return render(request, "signup.html")
def signupsuccess(request):
    return render(request,"signupsuccess.html")

def signupfailure(request): 
    user = request.user
    print(user.username)
    return render(request,"signupfailure.html")  
def players(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "players.html",context)
def win(request):
    user = request.user
    account = Account.objects.get(user=user)
    account.Balance = account.Balance+500
    print(account.Balance)
    account.save()
    return redirect('GamePage')
