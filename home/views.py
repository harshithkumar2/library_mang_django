from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login as log,logout
from .models import profile, book_details
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

@login_required(login_url='login')
def log_home(request):
    return render(request, 'login_home.html')

@login_required(login_url='login')
def book_dis(request):
    details = book_details.objects.filter(status=0)
    return render(request, 'book_display.html' ,{'data':details})

@login_required(login_url='login')
def book_rec(request):
    details = book_details.objects.all()
    return render(request, 'book_records.html', {'data': details})

def reg_data(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        mail = request.POST['mail']
        passw = request.POST['pass']
        rpass = request.POST['rpass']
        dob = request.POST['dob']
        gender = request.POST['gender']
        id_no = request.POST['id']
        if passw == rpass:
            user = User.objects.create_user(username=uname, first_name=fname, last_name=lname,email=mail, password=passw)
            user.save()
            profile.objects.create(user=user,gender= gender, dob=dob,id_no=id_no)
            return redirect('login')
        else:
            messages.error(request, 'Password Incorrect')
            return redirect('register')


def log_data(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['pass']
        user = authenticate(request, username=uname,password=passw)
        if user is not None:
            log(request, user)
            messages.info(request, f"You are now logged in as {uname}")
            return redirect('loghome')
        else:
            return redirect('login')

@login_required(login_url='login')
def logg_out(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def book_reg(request):
    if request.method == 'POST':
        book_no = request.POST['bno']
        book_name = request.POST['bname']
        book_taken = request.POST['btd']
        book_sub = request.POST['bsd']
        username = request.POST['uname']
        userid = request.POST['uid']
        fine = request.POST['fine']
        book_details.objects.create(book_no=book_no,book_name = book_name, btd=book_taken, bsd=book_sub,uname=username,uid=userid,fine=fine)
        messages.success(request, f'Book successfully added for {username}')
        return redirect('loghome')

def submitted(request):
    val = request.GET['val']
    book_details.objects.filter(id=val).update(status=1)
    return redirect('bookdis')






