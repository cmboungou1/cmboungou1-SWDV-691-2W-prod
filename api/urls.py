from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('goal-list/str:<user_id>/', views.goalList, name="goal-list"),
	path('goal-detail/str:<user_id>/<str:id>/', views.goalDetail, name="goal-detail"),
	path('goal-create/', views.goalCreate, name="goal-create"),
	path('goal-update/str:<user_id>/<str:id>/', views.goalUpdate, name="goal-update"),
	path('goal-delete/str:<user_id>/<str:id>/', views.goalDelete, name="goal-delete"),
]

