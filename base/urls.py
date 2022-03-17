from django.urls import URLPattern, path
from .views import (
    GoalList,
    GoalDetail,
    GoalCreate,
    GoalUpdate,
    DeleteView,
    CustomLoginView,
    RegisterPage,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", GoalList.as_view(), name="goals"),
    path("goal/<int:pk>/", GoalDetail.as_view(), name="goal"),
    path("goal-create/", GoalCreate.as_view(), name="goal-create"),
    path("goal-update/<int:pk>/", GoalUpdate.as_view(), name="goal-update"),
    path("goal-delete/<int:pk>/", DeleteView.as_view(), name="goal-delete"),
]
