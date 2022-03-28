from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GoalSerializer

from base.models import Goal
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/goal-list/',
		'Detail View':'/goal-detail/<str:pk>/',
		'Create':'/goal-create/',
		'Update':'/goal-update/<str:pk>/',
		'Delete':'/goal-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def goalList(request):
    try:
        goals = Goal.objects.all().order_by('-id')
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
def goalDetail(request, pk):
    try:
        goals = Goal.objects.get(id=pk)
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
        if serializer.is_valid():
            Response.status_code = 200
            serializer.save()
        else:
            Response.status_code = 404
        return Response(serializer.data)
    except:
        message = {
            "code":"400",
            "message":"Goal could not be created.",
        }
        Response.status_code = 400
        return Response(message)    

@api_view(['POST'])
def goalUpdate(request, pk):
    try:
        goal = Goal.objects.get(id=pk)
        serializer = GoalSerializer(instance=goal, data=request.data)

        if serializer.is_valid():
            serializer.save()
        Response.status_code = 200
        return Response(serializer.data)
    except:
        message = {
            "code":"400",
            "message":"Goal could not be Updated.",
        }
        Response.status_code = 400
        return Response(message) 

@api_view(['DELETE'])
def goalDelete(request, pk):
    try:
        goal = Goal.objects.get(id=pk)
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




