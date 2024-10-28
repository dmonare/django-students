from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('main/', views.main_page_view, name='main_page'),
    path('students/', views.students_page_view, name='students_page'),
] + debug_toolbar_urls()
