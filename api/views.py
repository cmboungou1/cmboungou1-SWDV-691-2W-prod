#from unicodedata import category
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GoalSerializer,GpaSerializer,SatSerializer
from base.models import GoalCategory, Gpa
from base.models import Sat
from base.models import Goal
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/goal-list/<str:user_id>/',
		'Detail View':'/goal-detail/<str:user_id>/<str:id>/',
		'Create':'/goal-create/',
		'Update':'/goal-update/<str:user_id>/<str:id>/',
		'Delete':'/goal-delete/<str:user_id>/<str:id>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def goalList(request,user_id):
    print(request)
    try:
        queryset= Goal.objects.all()
        print(queryset)
        #goals = Goal.objects.filter(category="GPA")
        goals = queryset.filter(user=user_id)
        serializer = GoalSerializer(goals, many=True)
        Response.status_code = 200
        return Response(serializer.data)
    except:
        message = {
            "code":"404",
            "message":"User record not found.",
        }
        Response.status_code = 404
        return Response(message)

# @api_view(['GET'])
# def goalDetail(request, pk): 
# 	goals = Goal.objects.get(id=pk)
# 	serializer = GoalSerializer(goals, many=False)
# 	return Response(serializer.data)

@api_view(['GET'])
def goalDetail(request,user_id, id):
    try:
        goals = Goal.objects.get(user=user_id,id=id)
        serializer = GoalSerializer(goals, many=False)
        Response.status_code = 200       
        return Response(serializer.data)
    except:
        message = {
            "code":"404",
            "message":"User record not found.",
        }
        Response.status_code = 404
        return Response(message)

@api_view(['POST'])
def goalCreate(request):
    try:
        serializer = GoalSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            goal = serializer.save()
            if goal.category == GoalCategory.GPA:
                print("In GPA")
                Gpa.objects.create(goal=goal,current_gpa=request.data["current_gpa"],library_hours=request.data["library_hours"],friends_with_high_gpa=request.data["friends_with_high_gpa"],office_hours=request.data["office_hours"])
            else:
                print("In SAT")
                Sat.objects.create(goal=goal,practice_test_score=request.data["practice_test_score"],private_tutor_time=request.data["private_tutor_time"],have_a_strategy=request.data["have_a_strategy"])
            Response.status_code = 200
        else:
            Response.status_code = 400
        return Response(serializer.data)
    except:
        message = {
            "code":"400",
            "message":"Goal could not be created. make sure to include all required fields.",
        }
        Response.status_code = 400
        return Response(message)    

@api_view(['POST'])
def goalUpdate(request, user_id, id):
    try:
        goal = Goal.objects.get(user=user_id, id=id)
        serializer = GoalSerializer(instance=goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data["category"] == "SAT":
                print("In SAT")
                sat = goal.sat
                sat.practice_test_score = request.data["practice_test_score"]
                sat.private_tutor_time = request.data["private_tutor_time"]
                sat.have_a_strategy = request.data["have_a_strategy"]
                sat.save()
            if request.data["category"] == "GPA":
                print("In GPA")
                gpa = goal.gpa
                gpa.current_gpa = request.data["current_gpa"]
                gpa.library_hours=request.data["library_hours"]
                gpa.friends_with_high_gpa=request.data["friends_with_high_gpa"]
                gpa.office_hours=request.data["office_hours"]
                gpa.save()
            Response.status_code = 200
        return Response(serializer.data)
    except:
        message = {
            "code":"404",
            "message":"Goal could not be Updated.",
        }
        Response.status_code = 404
        return Response(message) 

@api_view(['DELETE'])
def goalDelete(request, user_id, id):
    try:
        goal = Goal.objects.get(user=user_id,id=id)
        goal.delete()
        Response.status_code = 200
        return Response('Item succsesfully delete!')
    except:
        message = {
            "code":"400",
            "message":"Id does not exsit.",
        }
        Response.status_code = 400
        return Response(message) 




