
from django.urls import path


from aplicatie2 import views

app_name = 'aplicatie2'
urlpatterns = [
        path('adaugare/', views.CreateCompaniesView.as_view(), name='adaugare'),
        path('', views.CompaniesView.as_view(), name='lista_companii'),
        path('<int:pk>/modificare/', views.UpdateCompaniesView.as_view(), name='modifica'),
        # path('<int:pk>/sterge/', views.delete_companies, name='sterge'),
        # path('<int:pk>/dezactiveaza/', views.deactivate_companies, name='dezactiveaza'),
        # path('<int:pk>/activeaza/', views.activate_companies, name='activeaza'),
    ]