from django.contrib.auth import get_user_model
from .models import * 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.core import validators
from django.utils import timezone
from django.db.models import Q
import time
class RegistrationForm (UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    thumb = forms.ImageField(label='Attach a Passport Photograph',required=True,widget=forms.FileInput(attrs={'class':'form-control mt-2'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1', 'password2','thumb')

class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':True, 'placeholder':'Username Here', 'class':'form-control'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))
 
class EmployeeForm (forms.ModelForm):
    thumb = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=Employee.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))
    language = forms.ChoiceField(choices=Employee.LANGUAGE,widget=forms.Select(attrs={'class':'form-control'}))
    
    # role = forms.ChoiceField(choices = User.ROLE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'mobile','email','emergency','salary','gender','department','bank','nuban','language','thumb')
        widgets={
            'salary':forms.TextInput(attrs={'class':'form-control'}),
            'bank':forms.TextInput(attrs={'class':'form-control'}),
            'nuban':forms.TextInput(attrs={'class':'form-control'})
        }
    
    # def form_valid(self, form):
    #     form.instance.owner_id = 2
    #     return super(NodeCreateView, self).form_valid(form)



class EmployeeForm2 (UserCreationForm,forms.ModelForm):


    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    thumb = forms.ImageField(label='Attach a Passport Photograph',required=True,widget=forms.FileInput(attrs={'class':'form-control mt-2'}))
   
   
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
   
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=Employee.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))
    language = forms.ChoiceField(choices=Employee.LANGUAGE,widget=forms.Select(attrs={'class':'form-control'}))
    
    salary = forms.IntegerField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'salary'}))
    bank = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'bank'}))
    nuban = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nuban'}))
    
    class Meta:
        model = get_user_model()
    
        fields = ('username','first_name', 'last_name', 'mobile','email','emergency','salary','gender','department','bank','nuban','language','thumb','password1', 'password2')
        widgets={
        }


class EmployeeForm4 (forms.ModelForm):
    

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    thumb = forms.ImageField(label='Attach a Passport Photograph',required=True,widget=forms.FileInput(attrs={'class':'form-control mt-2'}))
   
   
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
   
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=Employee.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))
    language = forms.ChoiceField(choices=Employee.LANGUAGE,widget=forms.Select(attrs={'class':'form-control'}))
    
    bank = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'bank'}))
    nuban = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nuban'}))
    
    class Meta:
        model = Employee
    
        fields = ('username','first_name', 'last_name', 'mobile','email','emergency','gender','department','bank','nuban','language','thumb')
        widgets={
        }

class EmployeeForm3 (forms.ModelForm):
    

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    thumb = forms.ImageField(label='Attach a Passport Photograph',required=True,widget=forms.FileInput(attrs={'class':'form-control mt-2'}))
   
   
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
   
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=Employee.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))
    language = forms.ChoiceField(choices=Employee.LANGUAGE,widget=forms.Select(attrs={'class':'form-control'}))
    
    salary = forms.IntegerField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'salary'}))
    bank = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'bank'}))
    nuban = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nuban'}))
    
    class Meta:
        model = Employee
    
        fields = ('username','first_name', 'last_name', 'mobile','email','emergency','salary','gender','department','bank','nuban','language','thumb')
        widgets={
        }

class EmployeeCasting (forms.ModelForm):
    

    # employee = forms.ModelChoiceField(Employee.objects.all(),required=True, empty_label='Select an employee',widget=forms.Select(attrs={'class':'form-control'}))
   
    customer = forms.ModelChoiceField(Customer.objects.all(),required=True, empty_label='Select a cusomer',widget=forms.Select(attrs={'class':'form-control'}))
   
    quantity_of_concrete_cube = forms.IntegerField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Quantity of concrete cube'}))
    location = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'location'}))
    date_of_casting = forms.DateInput(attrs={'class':'form-control','type':'datetime-local'})
    

    class Meta:
        model = ConcreteCasting
    
        fields = ('customer', 'quantity_of_concrete_cube', 'location','date_of_casting')
        widgets={
        
            'date_of_casting': forms.DateInput(attrs={'class':'form-control','type':'datetime-local'}),
        }



class EmployeeIndividualUpdateCasting (forms.ModelForm):
    

    # employee = forms.ModelChoiceField(Employee.objects.all(),required=True, empty_label='Select an employee',widget=forms.Select(attrs={'class':'form-control'}))
   
    # customer = forms.ModelChoiceField(Customer.objects.all(),required=True, empty_label='Select a cusomer',widget=forms.Select(attrs={'class':'form-control'}))
   
    quantity_of_concrete_cube = forms.IntegerField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Quantity of concrete cube'}))
    # location = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'location'}))
    # date_of_casting = forms.DateInput(attrs={'class':'form-control','type':'date'})
    

    class Meta:
        model = ConcreteCasting
    
        fields = ('quantity_of_concrete_cube',)
        widgets={
        
            
        }


class EmployeeCouponPdfForm (forms.ModelForm):
    

    # employee = forms.ModelChoiceField(Employee.objects.all(),required=True, empty_label='Select an employee',widget=forms.Select(attrs={'class':'form-control'}))
   
    # user = forms.ModelChoiceField(User.objects.all(),required=True, empty_label='Select a cusomer',widget=forms.Select(attrs={'class':'form-control'}))
   
    description = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'description'}))
    # pdf_file = forms.FileField()
    class Meta:
        model = EmployeeCouponPdf
    
        fields = ('description', 'pdf_file')
        widgets={
        }

     
    


class KinForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    employee = forms.ModelChoiceField(Employee.objects.filter(kin__employee=None),required=False,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Kin
        fields = '__all__'
    


class DepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}))
    history = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief Department History'}))
    
    class Meta:
        model = Department
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Customer Name'}))
    mobile = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Customer Mobile'}))
    concrete_cube_price = forms.IntegerField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Concrete Cube Price'}))
    pump_opening_price = forms.IntegerField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pump Opening Price'}))
    class Meta:
        model = Customer
        fields = '__all__'
class AttendanceForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Attendance.STATUS,widget=forms.Select(attrs={'class':'form-control w-50'}))
    staff = forms.ModelChoiceField(Employee.objects.filter(Q(attendance__status=None) | ~Q(attendance__date = timezone.localdate())), widget=forms.Select(attrs={'class':'form-control w-50'}))
    class Meta:
        model = Attendance
        fields = ['status','staff']

class LeaveForm (forms.ModelForm):

    class Meta:
        model = Leave
        fields = '__all__'

        widgets={
            'start': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'end': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'employee':forms.Select(attrs={'class':'form-control'}),
        }
class RecruitmentForm(forms.ModelForm):
    class Meta:
        model=Recruitment
        fields = '__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
        }
    
        


class ExpensesForm(forms.ModelForm):
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))
    price = forms.IntegerField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}))
   
    class Meta:
        model = Expenses
        fields =['description','price']