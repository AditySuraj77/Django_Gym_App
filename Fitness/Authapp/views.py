from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Contact,MembershipPlan,Trainer,Enrollment,AttendenceSystem


# Create your views here.

def Home(request):
    return render(request,'home.html')

def SignUp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request,'Confirm Password Not Match')
            return redirect(SignUp)

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,'Username Already Exists Select Unique Username')
            return redirect(SignUp)

        user = User.objects.create(
            username = username,
        )

        user.set_password(password)

        user.save()
        messages.success(request,"Account Created Successfully")
        return redirect(SignUp)
    return render(request, 'signUp.html')


def LogIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        if not User.objects.filter(username = username).exists():
            messages.error(request,'Username Not Found ! ')
            return redirect(LogIn)

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request,'Incorrect Password ! ')

        else:
            login(request,user)
            return redirect(Home)
   

    return render(request,'LogIn.html')


def LogOut(request):
    logout(request)
    return redirect(LogIn)


def contact(request):
    if request.method == 'POST':
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Phone = request.POST.get("phone")
        Question = request.POST.get("question")
        
        query = Contact(name=Name,email=Email,phone=Phone,question=Question)
        query.save()
        messages.info(request,'Thanks for Contacting Us. We will get back you soon.')

    return render(request,'contact.html')


def Enrollments(request):


    if not request.user.is_authenticated:
        messages.info(request,'Login for Enrollment ! ')
        return redirect(LogIn)
    

    Membership = MembershipPlan.objects.all()
    GymTrainer = Trainer.objects.all()
    context = {"Membership":Membership,"GymTrainer":GymTrainer}

    if request.method == "POST":
        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        DoB = request.POST.get("DOB")
        plan = request.POST.get("plan")
        trainer = request.POST.get("trainer")
        reference = request.POST.get("Reference")
        address = request.POST.get("Address")
        query = Enrollment(Full_name=fullname,
                           User_Name = username,
                           email=email,
                           gender=gender,
                           phone_Number=phone,
                           DOB=DoB,
                           Select_MembershipPlan=plan, 
                           Select_Trainer=trainer,
                           reference=reference,
                           address=address)
        query.save()
        
        print(fullname,gender,email,phone,DoB,plan,trainer,reference,address)
        messages.success(request,"Enrollment Successful. ")
        return redirect(Enrollments)


    return render(request,'Enroll.html',context)



def Profile(request):

    if not request.user.is_authenticated:
        messages.info(request,'Login for View Profile ! ')
        return redirect(LogIn)

    user = request.user
    posts = Enrollment.objects.filter(User_Name=user)
    context = {"posts":posts}

    print(user)

    return render(request,'profile.html',context)


def Attendence(request):
    if not request.user.is_authenticated:
        messages.info(request,'Login for Attendence ! ')
        return redirect(LogIn)
    
    user = request.user
    attendence_details = AttendenceSystem.objects.filter(User_Name=user)
    GymTrainer = Trainer.objects.all()
    context = {"Trainer":GymTrainer,"attendence":attendence_details}
    
    if request.method == "POST":
        username = request.POST.get("username")
        logintime = request.POST.get("logintime")
        logouttime = request.POST.get("logouttime")
        WorkOut_type = request.POST.get("WorkOut_type")
        trainer = request.POST.get("trainer")
        query = AttendenceSystem(User_Name=username,
                                 Login_Time=logintime,
                                 Logout_Time=logouttime,
                                 Workout_Type=WorkOut_type,
                                 Trained_By=trainer)
        query.save()
        messages.success(request,'Attendence Applied ')
        return redirect(Attendence)
   
    return render(request,'attendence.html',context)


def Delete_attendence(request,delete_id):
    data = AttendenceSystem.objects.get(id=delete_id)
    data.delete()
    messages.info(request,'Item Deleted ! ')
    return redirect(Attendence)