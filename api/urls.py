from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('goal-list/', views.goalList, name="goal-list"),
	path('goal-detail/<str:pk>/', views.goalDetail, name="goal-detail"),
	path('goal-create/', views.goalCreate, name="goal-create"),
	path('goal-update/<str:pk>/', views.goalUpdate, name="goal-update"),
	path('goal-delete/<str:pk>/', views.goalDelete, name="goal-delete"),
]

