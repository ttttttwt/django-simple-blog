from django.contrib.auth import views as auth_views
from .froms import LoginForm
from django.urls import path
from . import views


urlpatterns = [
    path("hello/", views.say_hello),
    path("index/", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(authentication_form=LoginForm, template_name="login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('add-post/', views.add_post, name="add-post"),
    path('edit-post/<int:pk>', views.edit_post, name="edit-post"),
    path("detail-post/<int:pk>", views.detail_post, name="detail-post"),
    path("add-comment/<int:pk>", views.add_comment, name="add-comment")
]
