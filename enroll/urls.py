
from django.contrib import admin
from django.urls import path, re_path
from enroll import views
from django.urls import include


from enroll import views
from django.urls import include
from enroll.forms import LoginForm, MyPasswordChangeForm


from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from enroll.views import home

urlpatterns = [
    path('', home, name='home'),



    path('department/', views.department, name="department"),


    path('cse/', views.cse, name="cse"),
    path('entc/', views.entc, name="entc"),
    path('it/', views.it, name="it"),
    path('electrical/', views.electrical, name="electrical"),
    path('chemical/', views.chemical, name="chemical"),
    path('mech/', views.mech, name="mech"),
    path('production/', views.production, name="pro"),
    path('textile/', views.textile, name="textile"),
    path('civil/', views.civil, name="civil"),
    path('instru/', views.instru, name="instru"),







    #     path('admin/', admin.site.urls),

    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),

    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path('student/profile/', views.user_profile, name='profile'),
   
    path('accounts/login/', auth_views.LoginView.as_view(template_name='enroll/userlogin.html',
                                                         authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='enroll/passwordchange.html',
         form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='enroll/passwordchangedone.html'), name='passwordchangedone'),

    path("password-reset/", auth_views.PasswordResetView.as_view(
         template_name='enroll/password_reset.html'), name="password_reset"),
    path('password_reset/done/', auth_views. PasswordResetDoneView.as_view(
         template_name='enroll/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
         template_name='enroll/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
         template_name='enroll/password_reset_complete.html'), name='password_reset_complete'),







]
