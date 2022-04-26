from django.urls import URLPattern, path
from . import views
from django.contrib.auth.views import LogoutView
from .views import (
    CustomLoginView,
    RegisterPage,
    Timeline,
    View,
    Create,
    List,
    Edit,
)

# urlpatterns = [
#     path("login/", CustomLoginView.as_view(), name="login"),
#     path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
#     path("register/", RegisterPage.as_view(), name="register"),
#     path("goal/<int:pk>/", GoalDetail.as_view(), name="goal"),
#     path("goal-create/", GoalCreate.as_view(), name="goal-create"),
#     path("goal-update/<int:pk>/", GoalUpdate.as_view(), name="goal-update"),
#     path("goal-delete/<int:pk>/", DeleteView.as_view(), name="goal-delete"),
#     path("", GoalList.as_view(), name="goals"),
# ]

urlpatterns = [
    path("", CustomLoginView.as_view(), name="login"),
    path("list", List.as_view(), name="list"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("edit/", Edit.as_view(), name="edit"),
    path("view/", View.as_view(), name="view"),
    path("create/", Create.as_view(), name="create"),
    path("timeline/", Timeline.as_view(), name="timeline"),
]
