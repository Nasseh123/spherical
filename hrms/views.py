from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models  import (
    Employee, Department,Kin,
     Attendance, Leave, Recruitment,
     Customer,ConcreteCasting,Expenses,EmployeeCouponPdf,EmployeeChat)
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q,Sum
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .time_filter import gettime
import json

# Create your views here.
class Index(TemplateView):
   template_name = 'hrms/home/home.html'

#   Authentication
class Register (CreateView):
    model = get_user_model()
    form_class  = RegistrationForm
    template_name = 'hrms/registrations/register.html'
    success_url = reverse_lazy('hrms:login')
    
class Login_View(LoginView):
    model = get_user_model()
    form_class = LoginForm
    template_name = 'hrms/registrations/login.html'

    def get_success_url(self):
        url = resolve_url('hrms:dashboard')
        if self.request.user.role==1:
            url = resolve_url('hrms:dashboard')
        else:
            url = resolve_url('hrms:work_arrangeement_view')
        return url

class Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:login',permanent=True)
    
    
 # Main Board   
class Dashboard(LoginRequiredMixin,ListView):
    template_name = 'hrms/dashboard/index.html'
    login_url = 'hrms:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.filter(role=1).count()
        context['workers'] = Employee.objects.order_by('-id')
        print(context['workers'])
        return context

# Employee's Controller
class Employee_New(LoginRequiredMixin,CreateView):
    model = Employee  
    form_class = EmployeeForm2  
    template_name = 'hrms/employee/create.html'
    login_url = 'hrms:login'
    redirect_field_name = 'redirect:'
    
    success_url = reverse_lazy('hrms:employee_all')

    def form_valid(self, form):
        self.object = form.save()
        new_user = form.instance

        empl = self.model(mobile= form.cleaned_data['mobile'], emergency = form.cleaned_data['emergency'],gender=form.cleaned_data['gender'],department=form.cleaned_data['department'],language=form.cleaned_data['language'],nuban=form.cleaned_data['nuban'],bank=form.cleaned_data['bank'],salary =form.cleaned_data['salary'],user = new_user)
        empl.save()
        print(self.object)
        return HttpResponseRedirect(self.get_success_url())
    
# Employee's Controller

class Employee_Past_Arrangement(LoginRequiredMixin,DetailView):
    queryset = ConcreteCasting.objects.all()
    template_name = 'hrms/employee/single_pages/past_arrangement.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print(self.kwargs['pk'] )
            query = ConcreteCasting.objects.filter(employee=self.kwargs['pk'] )
            context["concretecasting"] = query

            queryset = Employee.objects.get(user=self.kwargs['pk'])
            print(queryset)
            context['employee'] = queryset

            # print(c)
            return context
        except ObjectDoesNotExist:
            return context
class Employee_All_Arrangement(LoginRequiredMixin,ListView):
    queryset = ConcreteCasting.objects.all()
    template_name = 'hrms/pages/employee/work_arrangement.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print(self.request.user.id)
            print()
            query = ConcreteCasting.objects.filter(employee=Employee.objects.get(user=self.request.user.id))
            print(query)
            context["concretecasting"] = query

            queryset = Employee.objects.get(user=self.request.user.id)
            print(queryset)
            print('*************************')
            
            context['employee'] = queryset

            # print(c)

            print('*************************')
            # CHECK IF ALREADY CHECKED IN
            # context["today"] = timezone.localdate()
            print(Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate()),staff=Employee.objects.get(user=self.request.user.id)) )
            pstaff = Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate()),staff=Employee.objects.get(user=self.request.user.id)) 
            context['present'] = pstaff
            print(pstaff)
            return context
        except ObjectDoesNotExist:
            return context
class Employee_Salary(LoginRequiredMixin,ListView):
    queryset = EmployeeAdvancePayment.objects.all()
    template_name = 'hrms/pages/employee/my_salary.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print(self.request.user.id)
            print()
            get_past_month_dates = gettime(0)
            query = EmployeeAdvancePayment.objects.filter(user=self.request.user.id,date_paid__range=[get_past_month_dates['first_day'], get_past_month_dates['last_day']])
            print(query)
            context["advancepayment"] = query

            # GET TOTAL DEDUCTIONS
            query2 = query.aggregate(Sum('amount'))
            context['advanceamount'] = query2['amount__sum']
            print(query2)
            queryset = Employee.objects.get(user=self.request.user.id)
            # print(queryset)
            context['employee'] = queryset
            pstaff = Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate()),staff=Employee.objects.get(user=self.request.user.id)) 
            context['present'] = pstaff
           

            # print(c)
            return context
        except ObjectDoesNotExist:
            return context




class Employee_CouponPdf(LoginRequiredMixin,ListView):
    queryset = EmployeeCouponPdf.objects.all()
    template_name = 'hrms/pages/employee/my_coupons.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print(self.request.user.id)
            print()
            # get_past_month_dates = gettime(0)
            query = EmployeeCouponPdf.objects.filter(user=self.request.user.id)
            print(query)
            context["allcouponpdf"] = query
            pstaff = Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate()),staff=Employee.objects.get(user=self.request.user.id)) 
            context['present'] = pstaff

            queryset = Employee.objects.get(user=self.request.user.id)
            context['employee'] = queryset
           

            return context
        except ObjectDoesNotExist:
            return context         
class Employee_New_Arrangement(LoginRequiredMixin,CreateView):
    model = ConcreteCasting  
    form_class = EmployeeCasting  
    template_name = 'hrms/employee/single_pages/new_arrangement.html'
    login_url = 'hrms:login'
    redirect_field_name = 'redirect:'
    # context_object_name = 'employee'
    
    success_url = reverse_lazy('hrms:employee_all') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print('*********************************')
            print(self.kwargs['pk'])
            queryset = Employee.objects.get(id=self.kwargs['pk'])
            context['employee'] = queryset
            return context
        except ObjectDoesNotExist:
            return context

    def form_valid(self, form):
        # form.instance.owner_id = 2
        print(form.instance.employee)
        self.object = form.save()
        new_arrangement = form.instance
        
        new_arrangement.employee_id =self.kwargs['pk'] 
        new_arrangement.save()
    
        print(self.object)



        return HttpResponseRedirect(self.get_success_url())


class Employee_Update_Arrangement(LoginRequiredMixin,UpdateView):
    model = ConcreteCasting  
    form_class = EmployeeCasting  
    template_name = 'hrms/employee/single_pages/edit_past_arrangement.html'
    login_url = 'hrms:login'
    # redirect_field_name = 'redirect:'

    # model = Employee
    # template_name = 'hrms/employee/edit.html'
    # form_class = EmployeeForm
    # login_url = 'hrms:login'
    context_object_name = 'employee'
    
    success_url = reverse_lazy('hrms:employee_all') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print('*********************************')
            print(self.kwargs['pk'])
            queryset = Employee.objects.get(id=self.kwargs['pk'])
            context['employee'] = queryset
            return context
        except ObjectDoesNotExist:
            return context

    # def form_valid(self, form):
    #     # form.instance.owner_id = 2
    #     print(form.instance.employee)
    #     self.object = form.save()
    #     new_arrangement = form.instance
        
    #     new_arrangement.employee_id =self.kwargs['pk'] 
    #     new_arrangement.save()
    
    #     print(self.object)



        return HttpResponseRedirect(self.get_success_url())
class Employee_All_Coupon_Pdf(LoginRequiredMixin,DetailView):
    template_name = 'hrms/employee/single_pages/coupon_pdf.html'
    queryset = Employee.objects.all()
    login_url = 'hrms:login'
    context_object_name = 'employee'
    

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print('****************dddd*****************')
            
            print(self.kwargs['pk'] )
        
            queryset = Employee.objects.get(id=self.kwargs['pk'])
            print('%%%%%%%%%%%%%%%%%%%%%')
            
            allcouponpdf = EmployeeCouponPdf.objects.filter(user=queryset.user.id)
            print(queryset)
            context['employee'] = queryset
            context['allcouponpdf'] = allcouponpdf

            # print(c)
            return context
        except ObjectDoesNotExist:
            return context

class Employee_New_CouponPdf(LoginRequiredMixin,CreateView):
    model = EmployeeCouponPdf  
    form_class = EmployeeCouponPdfForm  
    template_name = 'hrms/employee/single_pages/new_coupon_pdf.html'
    login_url = 'hrms:login'
    redirect_field_name = 'redirect:'
    # context_object_name = 'employee'
    
    success_url = reverse_lazy('hrms:employee_all') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print(self.kwargs['pk'])
            queryset = Employee.objects.get(id=self.kwargs['pk'])
            context['employee'] = queryset.user
            return context
        except ObjectDoesNotExist:
            return context

    def form_valid(self, form):
        # form.instance.owner_id = 2
        # print(form.instance.employee)
        self.object = form.save()
        new_arrangement = form.instance
        
        new_arrangement.user_id =self.kwargs['pk'] 
        new_arrangement.save()
    
        print(self.object)



        return HttpResponseRedirect(self.get_success_url())

class Employee_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/employee/index.html'
    model = Employee
    login_url = 'hrms:login'
    context_object_name = 'employees'
    paginate_by  = 5
    
class Employee_View(LoginRequiredMixin,DetailView):
    queryset = Employee.objects.select_related('department')
    template_name = 'hrms/employee/single_pages/profile.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context
        
# class Employee_Update(LoginRequiredMixin,UpdateView):
#     model = Employee
#     template_name = 'hrms/employee/edit.html'
#     form_class = EmplEmployeeForm2oyeeForm
#     login_url = 'hrms:login'
    
class Employee_Update(LoginRequiredMixin,UpdateView):
    model = Employee  
    form_class = EmployeeForm3  
    template_name = 'hrms/employee/edit.html'
    login_url = 'hrms:login'
    redirect_field_name = 'redirect:'
    
    success_url = reverse_lazy('hrms:employee_all')


    def get_initial(self, **kwargs):
        initial = super(Employee_Update, self).get_initial()
        query = Employee.objects.get(id=self.object.pk)
        print(query.mobile)
        initial['mobile'] = query.mobile
        initial['emergency'] = query.emergency
        initial['gender'] = query.gender
        initial['department'] = query.department
        initial['language'] = query.language
        initial['nuban'] = query.nuban
        initial['bank'] = query.bank
        initial['salary'] = query.salary

        initial['username'] = query.user.username
        initial['email'] = query.user.email
        initial['first_name'] = query.user.first_name
        initial['last_name'] = query.user.last_name
        
        

        return initial

    def form_valid(self, form):
        # self.object = form.save()
        new_user = form.instance
        query = Employee.objects.filter(id=self.object.pk)
        query.update(mobile= form.cleaned_data['mobile'], emergency = form.cleaned_data['emergency'],gender=form.cleaned_data['gender'],department=form.cleaned_data['department'],language=form.cleaned_data['language'],nuban=form.cleaned_data['nuban'],bank=form.cleaned_data['bank'],salary =form.cleaned_data['salary'])
    
        query2 = Employee.objects.get(id=self.object.pk)
        query3 = User.objects.filter(id=query2.user.id)
        query3.update(username= form.cleaned_data['username'], email = form.cleaned_data['email'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'])

        print(self.object)
        return HttpResponseRedirect(self.get_success_url())
class Employee_individual_Update(LoginRequiredMixin,UpdateView):
    model = Employee  
    form_class = EmployeeForm4
    template_name = 'hrms/pages/employee/edit_my_profile.html'
    login_url = 'hrms:login'
    redirect_field_name = 'redirect:'
    
    success_url = reverse_lazy('hrms:work_arrangeement_view')


    def get_initial(self, **kwargs):
        initial = super(Employee_individual_Update, self).get_initial()
        query = Employee.objects.get(id=self.object.pk)
        print(query)
        initial['mobile'] = query.mobile
        initial['emergency'] = query.emergency
        initial['gender'] = query.gender
        initial['department'] = query.department
        initial['language'] = query.language
        initial['nuban'] = query.nuban
        initial['bank'] = query.bank

        initial['username'] = query.user.username
        initial['email'] = query.user.email
        initial['first_name'] = query.user.first_name
        initial['last_name'] = query.user.last_name
        initial['thumb'] = query.user.thumb
        
        

        return initial

    def form_valid(self, form):
        # self.object = form.save()
        new_user = form.instance
        query = Employee.objects.filter(id=self.object.pk)
        query.update(mobile= form.cleaned_data['mobile'], emergency = form.cleaned_data['emergency'],gender=form.cleaned_data['gender'],department=form.cleaned_data['department'],language=form.cleaned_data['language'],nuban=form.cleaned_data['nuban'],bank=form.cleaned_data['bank'])
    
        query2 = Employee.objects.get(id=self.object.pk)
        query3 = User.objects.filter(id=query2.user.id)
        query3.update(username= form.cleaned_data['username'], email = form.cleaned_data['email'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'])

        print(self.object)
        return HttpResponseRedirect(self.get_success_url())

class Employee_individual_Update_casting(LoginRequiredMixin,UpdateView):
    # model = Employee  
    # form_class = EmployeeForm4
    # template_name = 'hrms/employee/pages/update_work_arrangement.html'
    # login_url = 'hrms:login'
    # redirect_field_name = 'redirect:'
    
    # success_url = reverse_lazy('hrms:employee_all')



    model = ConcreteCasting  
    form_class = EmployeeIndividualUpdateCasting  
    template_name = 'hrms/pages/employee/update_work_arrangement.html'
    login_url = 'hrms:login'
    
    success_url = reverse_lazy('hrms:work_arrangeement_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            print('*********************************')
            print(self.kwargs['pk'])
            queryset = Employee.objects.get(id=self.kwargs['pk'])
            context['employee'] = queryset
            return context
        except ObjectDoesNotExist:
            return context

    # def form_valid(self, form):
    #     # self.object = form.save()
    #     new_user = form.instance
    #     query = Employee.objects.filter(id=self.object.pk)
    #     query.update(mobile= form.cleaned_data['mobile'], emergency = form.cleaned_data['emergency'],gender=form.cleaned_data['gender'],department=form.cleaned_data['department'],language=form.cleaned_data['language'],nuban=form.cleaned_data['nuban'],bank=form.cleaned_data['bank'],salary =form.cleaned_data['salary'])
    
    #     query2 = Employee.objects.get(id=self.object.pk)
    #     query3 = User.objects.filter(id=query2.user.id)
    #     query3.update(username= form.cleaned_data['username'], email = form.cleaned_data['email'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'])

    #     print(self.object)
    #     return HttpResponseRedirect(self.get_success_url())
    
    
class Employee_Delete(LoginRequiredMixin,DeleteView):
    pass

class Employee_Kin_Add (LoginRequiredMixin,CreateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_add.html'
    login_url = 'hrms:login'
   

    def get_context_data(self):
        context = super().get_context_data()
        if 'id' in self.kwargs:
            emp = Employee.objects.get(pk=self.kwargs['id'])
            context['emp'] = emp
            return context
        else:
            return context

class Employee_Kin_Update(LoginRequiredMixin,UpdateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_update.html'
    login_url = 'hrms:login'

    def get_initial(self):
        initial = super(Employee_Kin_Update,self).get_initial()
        
        if 'id' in self.kwargs:
            emp =  Employee.objects.get(pk=self.kwargs['id'])
            initial['employee'] = emp.pk
            
            return initial

#Department views

class Department_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Department_New (LoginRequiredMixin,CreateView):
    model = Department
    template_name = 'hrms/department/create.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'

class Department_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')

#Customer views

class Customer_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/customer/index.html'
    model = Customer
    login_url = 'hrms:login'
    context_object_name = 'customers'
    paginate_by  = 5


class Customer_View(LoginRequiredMixin,DetailView):
    queryset = Customer.objects.all()
    template_name = 'hrms/customer/single.html'
    context_object_name = 'customer'
    login_url = 'hrms:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = ConcreteCasting.objects.filter(customer=self.object.pk)
            context["concretecasting"] = query
            return context
        except ObjectDoesNotExist:
            return context

class Customer_New (LoginRequiredMixin,CreateView):
    model = Customer
    template_name = 'hrms/customer/create.html'
    form_class = CustomerForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:cust_all')

    success_url = reverse_lazy('hrms:cust_all')
class Customer_Update(LoginRequiredMixin,UpdateView):
    model = Customer
    template_name = 'hrms/customer/edit.html'
    form_class = CustomerForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:cust_all')

#Attendance View

class Attendance_New (LoginRequiredMixin,CreateView):
    model = Attendance
    form_class = AttendanceForm
    login_url = 'hrms:login'
    template_name = 'hrms/attendance/create.html'
    success_url = reverse_lazy('hrms:attendance_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.localdate()
        pstaff = Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate())) 
        context['present_staffers'] = pstaff
        return context

class Attendance_Out(LoginRequiredMixin,View):
    login_url = 'hrms:login'

    def get(self, request,*args, **kwargs):

       user=Attendance.objects.get(Q(staff__id=self.kwargs['pk']) & Q(status='PRESENT')& Q(date=timezone.localdate()))
       user.last_out=timezone.localtime()
       user.save()
       return redirect('hrms:attendance_new')   

class LeaveNew (LoginRequiredMixin,CreateView, ListView):
    model = Leave
    template_name = 'hrms/leave/create.html'
    form_class = LeaveForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:leave_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leaves"] = Leave.objects.all()
        return context

class Payroll(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'hrms/payroll/index.html'
    login_url = 'hrms:login'
    context_object_name = 'stfpay'

class RecruitmentNew (CreateView):
    model = Recruitment
    template_name = 'hrms/recruitment/index.html'
    form_class = RecruitmentForm
    success_url = reverse_lazy('hrms:recruitment')

class RecruitmentAll(ListView):
    model = Recruitment
    login_url = 'hrms:login'
    template_name = 'hrms/recruitment/all.html'
    context_object_name = 'recruit'

    paginate_by = 3 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['recruit'] =context
        context['now'] = timezone.now()
        return context

class RecruitmentDelete (LoginRequiredMixin,View):
    login_url = 'hrms:login'
    def get (self, request,pk):
     form_app = Recruitment.objects.get(pk=pk)
     form_app.delete()
     return redirect('hrms:recruitmentall', permanent=True)

class Pay(LoginRequiredMixin,ListView):
    model = Employee
    template_name = 'hrms/payroll/index.html'
    context_object_name = 'emps'
    login_url = 'hrms:login'




# EXPENSES

class Expenses_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/expenses/index.html'
    model = Expenses
    login_url = 'hrms:login'
    context_object_name = 'expenses'
    paginate_by  = 5


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        time= gettime(0) #ZERO IS representing the curenting month....
        context["price"] = Expenses.objects.filter(date_created__range=[time['first_day'], time['last_day']]).aggregate(Sum('price'))

        print(context['price'])
        print(Expenses.objects.filter(date_created__range=[time['first_day'], time['last_day']]))
       
        return context

class Expenses_New (LoginRequiredMixin,CreateView):
    model = Expenses
    template_name = 'hrms/expenses/create.html'
    form_class = ExpensesForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:expenses_all')
    
    
    def form_valid(self, form):
            # form.instance.owner_id = 2
        # print(form.instance.employee)
        self.object = form.save()
        new_expense = form.instance
        
        new_expense.user =self.request.user
        new_expense.save()

    


        return HttpResponseRedirect(self.get_success_url())



# EMPLOYEE ADVANCE

# class Employee_Advance (LoginRequiredMixin,CreateView):
def Employee_Advance(request):
    # print 'RECEIVED REQUEST: ' + request.method
    if request.method == 'POST':
        # print 'Hello'
        print()
        EmployeeAdvancePayment.objects.create(amount= request.POST.get('amount', ''),user_id= request.POST.get('user_id', ''))
        return HttpResponse({'USER ADVANCE CREATED SUCCESSFULLY'}, content_type="application/json")
    else: #GET
        return render(request, 'buttonExample.html')

     
def Employee_CheckIn(request):
        # print 'RECEIVED REQUEST: ' + request.method
    if request.method == 'POST':
        # print 'Hello'
        print(request.POST.get('user_id', ''))
        Attendance.objects.create(status= 'PRESENT',staff= Employee.objects.get(user=request.POST.get('user_id', '')))
        return HttpResponse({'check in SUCCESSFULLY'}, content_type="application/json")
    else: #GET
        return HttpResponse()
   
def getFilteredExpenseDate(request):
    if request.method == 'GET':
        no_of_months = request.GET['no_of_months']
        time= gettime(int(no_of_months)) #ZERO IS representing the curenting month....
        price =Expenses.objects.filter(date_created__range=[time['first_day'], time['last_day']]).aggregate(Sum('price'))
        print(price)
        return HttpResponse(json.dumps(price), content_type="application/json")
    else:
           return HttpResponse("Request method is not a GET")



def room(request,pk):
    # username = request.GET.get('username')
    # room_details = Room.objects.get(name=room)
    print(request.user)
    employee =  Employee.objects.get(id=pk)
    print(employee)
    return render(request, 'hrms/employee/single_pages/chat.html',{
        'employee': employee
    })

def getMessages(request, employee_id):
    print(employee_id)
    room_details = EmployeeChat.objects.filter(employee = employee_id).values('user__first_name','user__last_name','date_created','message')

    # messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({"messages":list(room_details)})


def send(request):
    message = request.POST['message']
    employee = request.POST['employee']

    new_message = EmployeeChat.objects.create(message=message, user=request.user, employee_id=employee)
    new_message.save()
    return HttpResponse('Message sent successfully')



def updatepaid(request):
    # message = request.POST['message']
    employee = request.POST['employee']

    new_message = ConcreteCasting.objects.filter(employee_id=employee).update(paid=True)
    
    return JsonResponse({"message":"success"})

# $$$$$$$$$$$$$$44
def individual_room(request):
    employee =  Employee.objects.get(user=request.user.id)
    pstaff = Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate()),staff=Employee.objects.get(user=request.user.id)) 
    # context['present'] = pstaff
    return render(request, 'hrms/pages/employee/my_chat.html',{
        'employee': employee,
        'present':pstaff
    })

def getSpecMessages(request):
    
    room_details = EmployeeChat.objects.filter(employee =  Employee.objects.get(user=request.user.id)).values('user__first_name','user__last_name','date_created','message')

    return JsonResponse({"messages":list(room_details)})


def sendSpec(request):
    message = request.POST['message']
    employee = request.POST['employee']

    new_message = EmployeeChat.objects.create(message=message, user=request.user, employee_id=employee)
    new_message.save()
    return HttpResponse('Message sent successfully')