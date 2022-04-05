from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('goal-list/<int:user_id>/', views.goalList, name="goal-list"),
	path('goal-detail/<int:user_id>/<int:id>/', views.goalDetail, name="goal-detail"),
	path('goal-create/', views.goalCreate, name="goal-create"),
	path('goal-update/<int:user_id>/<int:id>/', views.goalUpdate, name="goal-update"),
	path('goal-delete/<int:user_id>/<int:id>/', views.goalDelete, name="goal-delete"),
]

