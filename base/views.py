from dataclasses import field, fields
from multiprocessing import context
from pydoc import describe
from pyexpat import model
from re import template
from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Goal


def list(request):
    return render(request, 'goal_list.html')

def edit(request):
    return render(request, 'goal_edit.html')

def view(request):
    return render(request, 'goal_view.html')

def create(request):
    return render(request, 'goal_create.html')

def timeline(request):
    return render(request, 'timeline.html')

# class RegisterPage(FormView):
#     template_name = "base/register.html"
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy("goals")

#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)

#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect("goals")
#         return super(RegisterPage, self).get(*args, **kwargs)







# class CustomLoginView(LoginView):
#     template_name = "base/login.html"
#     fields = "__all__"
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy("goals")


# class RegisterPage(FormView):
#     template_name = "base/register.html"
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy("goals")

#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)

#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect("goals")
#         return super(RegisterPage, self).get(*args, **kwargs)


# class GoalList(LoginRequiredMixin, ListView):
#     model = Goal
#     context_object_name = "goals"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["goals"] = context["goals"].filter(user=self.request.user)
#         context["count"] = context["goals"].filter(complete=False).count()
#         search_input = self.request.GET.get("search-area") or ""
#         if search_input:
#             context["goals"] = context["goals"].filter(title__startswith=search_input)

#         context["search_input"] = search_input

#         return context


# class GoalDetail(LoginRequiredMixin, DetailView):
#     model = Goal
#     context_object_name = "goal"
#     template_name = "base/goal.html"


# class GoalCreate(LoginRequiredMixin, CreateView):
#     model = Goal
#     fields = ["title", "description", "complete"]
#     success_url = reverse_lazy("goals")

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(GoalCreate, self).form_valid(form)


# class GoalUpdate(LoginRequiredMixin, UpdateView):
#     model = Goal
#     fields = ["title", "description", "complete"]
#     success_url = reverse_lazy("goals")


# class DeleteView(LoginRequiredMixin, DeleteView):
#     model = Goal
#     context_object_name = "goal"
#     success_url = reverse_lazy("goals")
