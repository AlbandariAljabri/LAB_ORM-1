from django.urls import path
from . import views

app_name = "blog"


urlpatterns = [
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("", views.read_blog_view, name="read_blog_view"),
    path("detail/<blog_id>/", views.blog_detail_view, name="blog_detail_view"),
    path("update/<blog_id>/", views.update_blog_view, name="update_blog_view"),
    path("delete/<blog_id>", views.delete_blog_view , name="delete_blog_view"),
  #  path("find/<blog_id>", views.find_page_view , name="find_page_view"), 

]
