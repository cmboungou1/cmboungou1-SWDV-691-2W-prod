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
	goals = Goal.objects.all().order_by('-id')
	serializer = GoalSerializer(goals, many=True)
	return Response(serializer.data)

# @api_view(['GET'])
# def goalDetail(request, pk): 
# 	goals = Goal.objects.get(id=pk)
# 	serializer = GoalSerializer(goals, many=False)
# 	return Response(serializer.data)

@api_view(['GET'])
def goalDetail(request, pk):
    message = {
        "code":"404",
        "message":"invalid id",
    }
    goals = Goal.objects.get(id=pk)
    serializer = GoalSerializer(goals, many=False)    
    #return Response(serializer.data) if goals else Response(message)
    return Response(message)

@api_view(['POST'])
def goalCreate(request):
	serializer = GoalSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def goalUpdate(request, pk):
	goal = Goal.objects.get(id=pk)
	serializer = GoalSerializer(instance=goal, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def goalDelete(request, pk):
	goal = Goal.objects.get(id=pk)
	goal.delete()

	return Response('Item succsesfully delete!')




