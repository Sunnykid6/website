'''
	whenever we want to add a new page to our site
	have to add a new path with the name of the extension as 
	well as the views.py method that renders the page with 
	forms if it has any.
'''
from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.aboutme, name="aboutme"),
    #path("register", views.register, name="register"),
    #path("logout", views.logout_request, name="logout"),
    #path("login", views.login_request, name="login"),
    path("projects", views.projects, name="projects"),
    path("gallery", views.gallery, name="gallery"),
    path("contact", views.contact, name="contact"),
    path("<single_slug>", views.single_slug, name="single_slug"),
]
