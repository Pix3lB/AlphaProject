from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from GamePage.models import Account

def GamePage(request):
    user = request.user
    account = Account.objects.get(user=user)
    print("account",account)
    balance = account.Balance
    return render(request, "GamePage.html",{'balance':balance})
def Pyscript(request):
    return render (request,"Pyscript.html")


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
        username = request.POST["username"]
        password = request.POST["password"]
        Balance=1000
        user = User.objects.create_user(username=username, password=password)
        account = Account.objects.create(user=user)
        user.save()
        messages.success(request, "Welcome! You now have an account")
        return redirect('HomePage')
    return render(request, "signup.html")
