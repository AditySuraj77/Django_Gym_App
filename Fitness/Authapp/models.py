from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    question = models.TextField() 


    def __str__(self):
        return self.email
    
 
class Enrollment(models.Model):
    Full_name = models.CharField(max_length=50)
    User_Name = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField()
    gender= models.CharField(max_length=12)
    phone_Number = models.CharField(max_length=11)
    DOB = models.CharField(max_length=50)
    Select_MembershipPlan = models.CharField(max_length=200)
    Select_Trainer = models.CharField(max_length=20)
    reference = models.CharField(max_length=50)
    address = models.TextField()
    Payment_Status = models.CharField(max_length=50, blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    Due_Date = models.DateField(blank=True,null=True)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.Full_name
    

class Trainer(models.Model):
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Phone = models.CharField(max_length=11)
    Salary = models.IntegerField()
    TimeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.Name
    

class MembershipPlan(models.Model):
    Plan = models.CharField(max_length=150)
    Price = models.IntegerField()

    def __str__(self):
        return f"{self.Plan,self.Price}"
    
    

class AttendenceSystem(models.Model):
    User_Name = models.CharField(max_length=20,blank=False,null=False)
    Login_Time = models.CharField(max_length=50)
    Logout_Time = models.CharField(max_length=50)
    Workout_Type = models.CharField(max_length=50)
    Trained_By = models.CharField(max_length=50)

    def __int__(self):
        return self.id