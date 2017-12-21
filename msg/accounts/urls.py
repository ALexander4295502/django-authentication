from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^logout/$", views.LougoutView.as_view(), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup")
]
