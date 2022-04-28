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
    neg_lib_hours_print = ""
    neg_friends_print = ""
    neg_office_print = ""
    pos_gpa_print = ""
    pos_sat_print = ""
    pos_tutor_print = ""
    pos_strategy_print = ""
    pos_lib_hours_print = ""
    pos_friends_print = ""
    pos_office_print = ""
    ave_gpa_print = ""
    ave_sat_print = ""
    ave_tutor_print = ""
    ave_strategy_print = ""
    ave_lib_hours_print = ""
    ave_friends_print = ""
    ave_office_print = ""
    total_sat = 0
    total_gpa = 0
    total_private_tutor_time = 0
    total_have_a_strategy = 0
    total_lib_hours = 0
    total_friends_with_high_gpa = 0
    total_office_hours = 0
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        queryset = Goal.objects.all()
        goals = queryset.filter(user=user_id) 
        def get_neg_impact(category):
            # gpa negative
            if category == "GPA":
                self.neg_gpa_print += ""+self.neg_gpa_print+" Your GPA is below average. We recommend that you spend time at the library during office hours and make friends with a high GPA if you haven't done so."
            # sat negative
            if category == "SAT":
                self.neg_sat_print += ""+self.neg_sat_print+" Your SAT practice test score is below average. We recommend hiring a private tutor and creating a test-taking strategy if you haven't done so."
            # tutor negative
            if category == "TUTOR":
                self.neg_tutor_print += ""+self.neg_tutor_print+" We recommend that you spend more time with an SAT tutor."
            # strategy negative 
            if category == "STRATEGY":
                self.neg_strategy_print += ""+self.neg_strategy_print+" Creating a test-tacking strategy can help you focus your time and improve productivity."
            # library hours negative
            if category == "LIB HOURS":
                self.neg_lib_hours_print += ""+self.neg_lib_hours_print+" Time at the library can help improve your grades." 
            # friends with high gpa
            if category == "FRIENDS":
                self.neg_friends_print += ""+self.neg_friends_print+" Spending time with successful people can have a positive influence." 
            # friends with high gpa
            if category == "OFFICE":
                self.neg_office_print += ""+self.neg_office_print+" We recommend reaching out to your teacher for office hours before it's too late."                                
        def get_pos_impact(category):
            # gpa positive
            if category == "GPA":
                self.pos_gpa_print += ""+self.pos_gpa_print+" Our data indicate that you're on track to be successful. Great job."
            # sat positive
            if category == "SAT":
                self.pos_sat_print += ""+self.pos_sat_print+" Things are looking very good! Good luck with your SAT."
            # tutor positive
            if category == "TUTOR":
                self.pos_tutor_print += ""+self.pos_tutor_print+" You should teach others. This will help you retain what you've learned."
            # strategy positive 
            if category == "STRATEGY":
                self.pos_strategy_print += ""+self.pos_strategy_print+" We are confident that your strategy will work out."
            # library hours positive 
            if category == "LIB HOURS":
                self.pos_lib_hours_print += ""+self.pos_lib_hours_print+" Don't give up your positive habits at the library."
            # friends positive 
            if category == "FRIENDS":
                self.pos_friends_print += ""+self.pos_friends_print+" Reciprocate favors with your inner circle. Keep your relationships relevant."
            # strategy positive 
            if category == "OFFICE":
                self.pos_office_print += ""+self.pos_office_print+" You don't need office hours at this point. Great Job"                                                
        def get_avrg_impact(category):
            # gpa average
            if category == "GPA":
                self.ave_gpa_print += ""+str(self.ave_gpa_print)+" Your GPA is average. Keep it up! If you keep on increasing your library hours, office hours, and good influences, we are sure you will hit a 4.0."
            # sat average
            if category == "SAT":
                self.ave_sat_print += ""+self.ave_sat_print+" Your SAT practice test score average. Keep it up!"
            # tutor average
            if category == "TUTOR":
                self.ave_tutor_print += ""+self.ave_tutor_print+" Good job so far. We recommend spending more time with an SAT tutor if you want to reach a higher score."
            # library hours average 
            if category == "LIB HOURS":
                self.ave_lib_hours_print += ""+self.ave_lib_hours_print+" The more time you spend at the library studying, the better."
            # friends average 
            if category == "FRIENDS":
                self.ave_friends_print += ""+self.ave_friends_print+" You have a few friends with high GPAs. Don't hesitate to make more."
            # strategy average 
            if category == "OFFICE":
                self.ave_office_print += ""+self.ave_office_print+" We are glad you are spending time with your teacher. Keep it up."    
        def impactMetrics():           
            gpa = 0
            sat = 0
            private_tutor_time = 0
            i = 0
            a = 0
            b = 0
            d = 0
            library_hours = 0
            friends_with_high_gpa = 0
            office_hours = 0
            e = 0
            x = 0
            for goal in goals:
                if goal.category == "GPA":
                    if goal.gpa.current_gpa:
                        i += 1
                        gpa += goal.gpa.current_gpa
                    if goal.gpa.library_hours:
                        d += 1                    
                        library_hours += goal.gpa.library_hours
                    if goal.gpa.friends_with_high_gpa:
                        e += 1                    
                        friends_with_high_gpa += goal.gpa.friends_with_high_gpa
                    if goal.gpa.office_hours:      
                        x += 1                    
                        office_hours += goal.gpa.office_hours      
                if goal.category == "SAT":
                    if goal.sat.practice_test_score:
                        a += 1
                        sat += goal.sat.practice_test_score
                    if goal.sat.private_tutor_time:
                        b += 1
                        private_tutor_time += goal.sat.private_tutor_time
                    if goal.sat.have_a_strategy == True :
                        self.total_have_a_strategy += 1
            # calculate the overall GPA
            self.total_gpa = gpa / i
            if self.total_gpa < 3.0 :
                get_neg_impact("GPA")
            elif self.total_gpa >= 3.0 and self.total_gpa <= 3.5 :
                get_avrg_impact("GPA") 
            elif self.total_gpa >= 3.5 :
                get_pos_impact("GPA")
            # library hours
            self.total_lib_hours = library_hours / d
            if self.total_lib_hours < 10 and self.total_gpa < 3.0 :
                get_neg_impact("LIB HOURS")
            elif self.total_gpa >= 3.0 and self.total_gpa <= 3.5 :
                get_avrg_impact("LIB HOURS") 
            elif self.total_sat >= 3.5 and self.total_lib_hours >= 10 :
                get_pos_impact("LIB HOURS")           
            # friends_with_high_gpa
            self.total_friends_with_high_gpa = friends_with_high_gpa / e
            if self.total_friends_with_high_gpa <= 0 and self.total_gpa < 3.0 :
                get_neg_impact("FRIENDS")
            elif self.total_friends_with_high_gpa == 1 or self.total_friends_with_high_gpa == 2 :
                get_avrg_impact("FRIENDS") 
            elif self.total_friends_with_high_gpa > 2 :
                get_pos_impact("FRIENDS")
            # office_hours
            self.total_office_hours = office_hours / x
            if self.total_office_hours < 10 and self.total_gpa < 3.0 :
                get_neg_impact("OFFICE")
            elif self.total_gpa >= 3.0 and self.total_gpa <= 3.5 :
                get_avrg_impact("OFFICE") 
            elif self.total_gpa >= 3.5 and self.total_office_hours >= 10 :
                get_pos_impact("OFFICE")
            # practice sat score metrics
            self.total_sat = sat / a
            if self.total_sat < 1040 :
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
        context['neg_impact'] = ""+self.neg_gpa_print+""+self.neg_sat_print+""
        context['pos_impact'] = ""+self.pos_gpa_print+""+self.pos_sat_print+""
        context['ave_impact'] = ""+self.ave_gpa_print+""+self.ave_sat_print+""

        context['neg_impact'] += "\n"+self.neg_tutor_print+""+self.neg_strategy_print+""
        context['pos_impact'] += "\n"+self.pos_tutor_print+""+self.pos_strategy_print+""
        context['ave_impact'] += "\n"+self.ave_tutor_print+""+self.ave_strategy_print+""

        context['neg_impact'] += "\n"+self.neg_lib_hours_print+""+self.neg_office_print+""
        context['pos_impact'] += "\n"+self.pos_lib_hours_print+""+self.pos_office_print+""
        context['ave_impact'] += "\n"+self.ave_lib_hours_print+""+self.ave_office_print+""

        context['neg_impact'] += "\n"+self.neg_friends_print+""
        context['pos_impact'] += "\n"+self.pos_friends_print+""
        context['ave_impact'] += "\n"+self.ave_friends_print+""

        return context

