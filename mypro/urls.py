


from django.contrib import admin
from django.urls import path
from enroll import urls
from django.urls import include



# from enroll.forms import LoginForm,MyPasswordChangeForm
# from enroll import views

# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns = [


     path('admin/', admin.site.urls),
     
     path('',include('enroll.urls'))
]

    # path('',include('myapp.urls')),


#      path('admin/', admin.site.urls),
#      path('profile/',views.profile,name="profile"),
  
#     #  path('add/addrecord/', views.addrecord, name='addrecord'),
#     # path('', views.index, name='index'),
#     # path('', views.add_show,name="addandshow"),
#     path('delete/<int:id>/',views.delete_data,name="deletedata"),
#     path('<int:id>/',views.update_data,name="updatedata"),
#     # re_path(r'^departments/(?P<departmentName>[\w\s]+)/$',views.picksub,name="picksub"),
#     # path('home/<my_id>',views.show_details,name="detail"),
#      path('subject/<data>',views.picksub,name="picksub"),
#      path('semester/<int:d>/',views.picksem,name="picksem"),
    
#      path('', views.display_subjects, name='display_subjects'),
#     path('app/', views.student_form, name='student_form'),

#     path('cse/',views.cse,name="cse"),
#     path('entc/',views.entc,name="entc"),
#     path('it/',views.it,name="it"),
#     path('electrical/',views.electrical,name="electrical"),
#     path('chemical/',views.chemical,name="chemical"),
#     path('mech/',views.mech,name="mech"),
#     path('production/',views.production,name="pro"),
#     path('textile/',views.textile,name="textile"),
#     path('civil/',views.civil,name="civil"),
#     path('instru/',views.instru,name="instru"),




#     # userauthentication 
#     path('admin/', admin.site.urls),
#     path('', views.home,name="home"),

#     path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

#     path('login/',views.user_login ,name='login'),
#     path('logout/',auth_views.LogoutView.as_view (next_page='login'),name="logout"),
#     path('profile/',views.user_profile, name='profile'),
#     path('home/',views.home,name='home'),
#     path('accounts/login/', auth_views.LoginView.as_view(template_name='enroll/userlogin.html', authentication_form=LoginForm), name='login'),
#     path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='enroll/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
#     path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='enroll/passwordchangedone.html'),name='passwordchangedone'),

#     path("password-reset/", auth_views.PasswordResetView.as_view(template_name='enroll/password_reset.html'), name="password_reset"),
#     path('password_reset/done/',auth_views. PasswordResetDoneView.as_view(template_name='enroll/password_reset_done.html'), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='enroll/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='enroll/password_reset_complete.html'), name='password_reset_complete'),

# ]

    







