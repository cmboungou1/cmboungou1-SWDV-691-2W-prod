from dataclasses import field, fields
from multiprocessing import context
from pydoc import describe
from pyexpat import model
from re import template
from urllib import request
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


class CustomLoginView(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("list")


class RegisterPage(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("login")
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    def form_valid(self, form):
        print("in heeer")
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("timeline")
        return super(RegisterPage, self).get(*args, **kwargs)

# def list(request):
#     return render(request, 'goal_list.html')
class List(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = "goal"
    template_name = "goal_list.html"

# def edit(request):
#     return render(request, 'goal_edit.html')
class Edit(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = "goal"
    template_name = "goal_edit.html"

# def view(request):
#     return render(request, 'goal_view.html')
class View(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = "goal"
    template_name = "goal_view.html"

# def create(request):
#     return render(request, 'goal_create.html')
class Create(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = "goal"
    template_name = "goal_create.html"

# def timeline(request):
#     return render(request, 'timeline.html')
class Timeline(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = "goal"
    template_name = "timeline.html"
    neg_gpa_print = ""
    neg_sat_print = ""
    neg_tutor_print = ""
    neg_strategy_print = ""
    pos_gpa_print = ""
    pos_sat_print = ""
    pos_tutor_print = ""
    pos_strategy_print = ""
    ave_gpa_print = ""
    ave_sat_print = ""
    ave_tutor_print = ""
    ave_strategy_print = ""
    total_sat = 0
    total_gpa = 0
    total_private_tutor_time = 0
    total_have_a_strategy = 0
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        queryset = Goal.objects.all()
        goals = queryset.filter(user=user_id) 
        def get_neg_impact(category):
            # gpa negative
            if category == "GPA":
                self.neg_gpa_print += ""+self.neg_gpa_print+" negative GPA"
            # sat negative
            if category == "SAT":
                self.neg_sat_print += ""+self.neg_sat_print+" negative SAT"
            # tutor negative
            if category == "TUTOR":
                self.neg_tutor_print += ""+self.neg_tutor_print+" negative TUTOR"
            # strategy negative 
            if category == "STRATEGY":
                self.neg_strategy_print += ""+self.neg_strategy_print+" negative STRATEGY"
        def get_pos_impact(category):
            # gpa positive
            if category == "GPA":
                self.pos_gpa_print += ""+self.pos_gpa_print+" positive GPA"
            # sat positive
            if category == "SAT":
                self.pos_sat_print += ""+self.pos_sat_print+" positive SAT"
            # tutor positive
            if category == "TUTOR":
                self.pos_tutor_print += ""+self.pos_tutor_print+" positive TUTOR"
            # strategy positive 
            if category == "STRATEGY":
                self.pos_strategy_print += ""+self.pos_strategy_print+" positive STRATEGY"
        def get_avrg_impact(category):
            # gpa average
            if category == "GPA":
                self.ave_gpa_print += ""+str(self.ave_gpa_print)+" average GPA"
            # sat average
            if category == "SAT":
                self.ave_sat_print += ""+str(self.ave_sat_print)+" average SAT"
            # tutor average
            if category == "TUTOR":
                self.ave_tutor_print += ""+self.ave_tutor_print+" average TUTOR"
        def impactMetrics():           
            gpa = 0
            sat = 0
            private_tutor_time = 0
            i = 0
            a = 0
            b = 0
            c = 0
            for goal in goals:
                if goal.category == "GPA":
                    i += 1
                    print(goal)
                    gpa += goal.gpa.current_gpa      
                if goal.category == "SAT":
                    print(goal)
                    a += 1
                    sat += goal.sat.practice_test_score
                    b += 1
                    private_tutor_time += goal.sat.private_tutor_time
                    c += 1
                    print("Have a strategy", goal.sat.have_a_strategy)
                    if goal.sat.have_a_strategy == True :
                        self.total_have_a_strategy += 1 
            # calculate the overall GPA
            self.total_gpa = gpa / i
            if self.total_gpa < 3.0 :
                print("3.0 this")
                get_neg_impact("GPA")
            elif self.total_sat >= 3.0 and self.total_sat <= 3.5 :
                get_avrg_impact("GPA") 
            elif self.total_sat >= 3.5 :
                print("3.5")
                get_pos_impact("GPA")
            # practice sat score metrics
            self.total_sat = sat / a
            if self.total_sat < 1040 :
                print("Sat99")
                get_neg_impact("SAT")
            elif self.total_sat >= 1040 and self.total_sat <= 1060 :
                get_avrg_impact("SAT") 
            elif self.total_sat > 1060:
                get_pos_impact("SAT")
            # private tutor hours
            self.total_private_tutor_time = private_tutor_time / b
            if self.total_private_tutor_time < 10 and self.total_sat < 1040 :
                get_neg_impact("TUTOR")
            elif self.total_sat >= 1040 and self.total_sat <= 1060 :
                get_avrg_impact("TUTOR") 
            elif self.total_sat > 1060 and self.total_private_tutor_time >= 80 :
                get_pos_impact("TUTOR")
            # do you have a strategy
            if self.total_have_a_strategy >= 1 :
                get_pos_impact("STRATEGY")
            else :
                get_neg_impact("STRATEGY") 
                    
        impactMetrics()
        print("hereeee", self.ave_sat_print)            
        context['neg_impact'] = ""+self.neg_gpa_print+""+self.neg_sat_print+""
        context['pos_impact'] = ""+self.pos_gpa_print+""+self.pos_sat_print+""
        context['ave_impact'] = ""+self.ave_gpa_print+""+self.ave_sat_print+""

        context['neg_impact'] += ""+self.neg_tutor_print+""+self.neg_strategy_print+""
        context['pos_impact'] += ""+self.pos_tutor_print+""+self.pos_strategy_print+""
        context['ave_impact'] += ""+self.ave_tutor_print+""+self.ave_strategy_print+""

        return context

