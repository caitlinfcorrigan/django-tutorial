from django.urls import path
from . import views

# Add namespace with app name for projects with multiple apps
app_name='polls'
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:question_id>/', views.details, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]