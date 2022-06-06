from django.urls import path
from . import views
app_name = 'hrms'
urlpatterns = [

# Authentication Routes
    path('', views.Index.as_view(), name='index'),
    path('register/', views.Register.as_view(), name='reg'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),

# Employee Routes
    path('dashboard/employee/', views.Employee_All.as_view(), name='employee_all'),
    path('dashboard/employee/new/', views.Employee_New.as_view(), name='employee_new'),
    path('dashboard/employee/<int:pk>/view/', views.Employee_View.as_view(), name='employee_view'),
    path('dashboard/employee/<int:pk>/update/', views.Employee_Update.as_view(), name='employee_update'),

    
    path('profile/update/<int:pk>', views.Employee_individual_Update.as_view(), name='employee_individual_update'),

 path('casting/update/<int:pk>', views.Employee_individual_Update_casting.as_view(), name='employee_individual_update_casting'),


    path('dashboard/employee/<int:pk>/delete/', views.Employee_Delete.as_view(), name='employee_delete'),
    path('dashboard/employee/<int:id>/kin/add/', views.Employee_Kin_Add.as_view(), name='kin_add'),
    path('dashboard/employee/<int:id>/kin/<int:pk>/update/', views.Employee_Kin_Update.as_view(), name='kin_update'),


    
    path('dashboard/employee/<int:pk>/newarrangeement/', views.Employee_New_Arrangement.as_view(), name='employee_new_arrangement'),
    path('dashboard/employee/<int:pk>/pastarrangeement/', views.Employee_Past_Arrangement.as_view(), name='employee_past_arrangement'),
 path('dashboard/employee/<int:pk>/updatearrangeement/', views.Employee_Update_Arrangement.as_view(), name='employee_update_arrangement'),


    path('dashboard/employee/<int:pk>/new_coupon_pdf/', views.Employee_New_CouponPdf.as_view(), name='employee_new_coupon_pdf'),
    path('dashboard/employee/<int:pk>/allcouponpdf/', views.Employee_All_Coupon_Pdf.as_view(), name='all_employee_coupon_pdf'),

    path('dashboard/employee/allcouponpdf/',views.Employee_CouponPdf.as_view(),name='individual_all_employee_coupon_pdf'),
#Department Routes
    path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
    path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
    path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),

#Attendance Routes
    path('dashboard/attendance/in/', views.Attendance_New.as_view(), name='attendance_new'),
    path('dashboard/attendance/<int:pk>/out/', views.Attendance_Out.as_view(), name='attendance_out'),

#Leave Routes

    path("dashboard/leave/new/", views.LeaveNew.as_view(), name="leave_new"),

#Recruitment

    path("recruitment/",views.RecruitmentNew.as_view(), name="recruitment"),
    path("recruitment/all/",views.RecruitmentAll.as_view(), name="recruitmentall"),
    path("recruitment/<int:pk>/delete/", views.RecruitmentDelete.as_view(), name="recruitmentdelete"),

#Payroll
    path("employee/pay/",views.Pay.as_view(), name="payroll"),

# CUSTOMER
    path('dashboard/customer/all/', views.Customer_All.as_view(), name='cust_all'),
    path('dashboard/customer/add/', views.Customer_New.as_view(), name='cust_new'),
    path('dashboard/customer/<int:pk>/update/', views.Customer_Update.as_view(), name='cust_update'),
    path('dashboard/customer/<int:pk>/view/', views.Customer_View.as_view(), name='cust_view'),


    # expenses
    path('dashboard/expenses/all/', views.Expenses_All.as_view(), name='expenses_all'),
    path('dashboard/expense/add/', views.Expenses_New.as_view(), name='expenses_new'),
    # path('dashboard/customer/<int:pk>/update/', views.Customer_Update.as_view(), name='cust_update'),

    path('total_expense', views.getFilteredExpenseDate, name='get_filtered_expense_date'),
    # total_expense


#EMPLOYEE ADVANCE
    path('employee_advance/', views.Employee_Advance, name='employee_advance'),



    path('employee_checkin/', views.Employee_CheckIn, name='employee_checkin'),




    # path('employee_advance/<int:pk>', views.Employee_Advance, name='employee_advance_view'),



    path('work_arrangeement/', views.Employee_All_Arrangement.as_view(), name='work_arrangeement_view'),
    path('employee_salary/', views.Employee_Salary.as_view(), name='employee_salary_view'),
    
    path('chat/<str:pk>', views.room, name='chatroom'),
    path('getMessages/<str:employee_id>/', views.getMessages, name='get_spec_messages'),
    path('send', views.send, name='send'),

    # INDIVIDUAL EMPLOYEE
    path('chat-spec/employer', views.individual_room, name='chat_employer'),
    path('getindividualMessages/employer', views.getSpecMessages, name='get_mes_employer'),
    path('send/employer', views.send, name='send'),

    path('update_paid', views.updatepaid, name='updatepaid'),
   

    
]
