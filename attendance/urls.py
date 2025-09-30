from django.urls import path
from . import views


urlpatterns =[
    path("login/",views.login_pg,name="login_page"),
    path("dashbort/",views.dashbor_pd,name="dashbort"),
    path("registerpage",views.register_pg,name="registerpage"),
    path("view/",views.view_attendance,name="view"),
    path("add/",views.add_students,name="add"),
    path("mark/",views. mark_the_attendance,name="mark"),
    path("logout_fu/",views.logout_pg,name="logout_fu"),
    path("report/",views.report_pg,name="report"),
    path("",views.home,name="home")
    
]