#from curses import meta
# from msilib.schema import Class
from django.db import models
import random
from django.urls import reverse
from django.utils import timezone
import time
from django.contrib.auth.models import AbstractUser


   
# Create your models here.
user_base_url = "uploads/users/"

class User(AbstractUser):
    thumb = models.ImageField(null=True)
    ADMINISTRATOR = 1
    EMPLOYEE = 2

      
    ROLE_CHOICES = (
          (ADMINISTRATOR, 'Administrator'),
          (EMPLOYEE, 'Employee'),
      )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True,default=EMPLOYEE)
    

class Customer(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False,default='fatme')
    mobile = models.CharField(max_length=15)
    concrete_cube_price = models.IntegerField(max_length=16,default='00,000.00')   
    pump_opening_price = models.IntegerField(max_length=16,default='00,000.00')   
    

    def __str__(self):
        return self.name



class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False,default='fatme')
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hrms:dept_detail", kwargs={"pk": self.pk})
    

class Employee(models.Model):
    LANGUAGE = (('english','ENGLISH'),('yoruba','YORUBA'),('hausa','HAUSA'),('french','FRENCH'))
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))

    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    # thumb = models.ImageField(blank=True,null=True)

    # first_name = models.CharField(max_length=50, null=False)
    # last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    # email = models.EmailField(max_length=125, null=False)
 
    address = models.TextField(max_length=100, default='')
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    # joined = models.DateTimeField(default=timezone.now)
    language = models.CharField(choices=LANGUAGE, max_length=10, default='english')
    nuban = models.CharField(max_length=10, default='0123456789')
    bank = models.CharField(max_length=25, default='First Bank Plc')
    salary = models.CharField(max_length=16,default='00,000.00')      

    
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.first_name
        
    def get_absolute_url(self):
        return reverse("hrms:employee_view", kwargs={"pk": self.pk})


class EmployeeAdvancePayment(models.Model):
    
  
    amount = models.IntegerField(default = 0)    
    date_paid = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.first_name



class ConcreteCasting(models.Model):
    
    date_of_casting = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=500)
    quantity_of_concrete_cube = models.IntegerField(default = 0)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.location
  
class Kin(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    occupation = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.first_name+'-'+self.last_name
    
    def get_absolute_url(self):
        return reverse("hrms:employee_view",kwargs={'pk':self.employee.pk})
   
class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField()
    last_out = models.TimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=15 )
    staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def save(self,*args, **kwargs):
        self.first_in = timezone.localtime()
        super(Attendance,self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)
    
class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start
    
class Recruitment(models.Model):
    first_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    position = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name +' - '+self.position
    # class Meta:
    #      abstract = True


class Expenses(models.Model):
    
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default = 0)
   
    def __str__(self):
        return self.description


def employee_coupon_pdf_path(self,filename):
    url = f"{user_base_url}{filename}"
    return url

class EmployeeCouponPdf(models.Model):
    
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    read  = models.BooleanField(default=False)
    pdf_file = models.FileField(upload_to=employee_coupon_pdf_path)
   
    def __str__(self):
        return self.description


class EmployeeChat(models.Model):
    
    
    STATUS = (('employer','employer'),('employee','employee'))

    message = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  #this resembles the employer that chatted witht the employee.
    
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    
    sender = models.CharField(choices=STATUS,  default='employer',max_length=15)  #employer THIS REPRESENTS USER COLUMN
   
    def __str__(self):
        return self.message