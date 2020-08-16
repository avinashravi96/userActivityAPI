from .models import User, Activity
from .serializers import MemberSerializer, UserSerializer, ActivitySerializer 
from rest_framework import generics, status, viewsets
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Method used to GET,POST and DELETE activities

@api_view(['GET', 'POST', 'DELETE'])
def activity_list(request):
    if request.method == 'GET':
        activity = Activity.objects.all()
        activity_serializer = ActivitySerializer(activity,many=True)
        return JsonResponse(activity_serializer.data, safe=False)
    elif request.method == "POST":
        activity_data = JSONParser().parse(request)
        activity_serializer = ActivitySerializer(data=activity_data)
        if activity_serializer.is_valid():
            activity_serializer.save()
            return JsonResponse(activity_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(activity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Activity.objects.all().delete()
        return JsonResponse({'message': '{} Activities were deleted successfully!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

# Method used to GET,UPDATE and DELETE activities by activity ID

@api_view(['GET', 'PUT', 'DELETE'])
def activity_detail(request, pk):
    try:
        activity = Activity.objects.get(pk=pk)
    except Activity.DoesNotExist:
        return JsonResponse({'message': 'The activity does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        activity_serializer = ActivitySerializer(activity)
        return JsonResponse(activity_serializer.data)

    elif request.method == 'PUT':
        activity_data = JSONParser().parse(request)
        activity_serializer = ActivitySerializer(activity, data=activity_data)
        if activity_serializer.is_valid():
            activity_serializer.save()
            return JsonResponse(activity_serializer.data)
        return JsonResponse(activity_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        activity.delete()
        return JsonResponse({'message': 'Activity was deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)

# Method used to GET,POST and DELETE Users

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user,many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

# Method used to GET,UPDATE and DELETE activities by User ID

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)

# Method used to GET list of users along with activity Data

@api_view(['GET'])
def members_list(request):
    if request.method == 'GET':
        members = User.objects.all()
        member_serializer = MemberSerializer(members,many=True)
        return JsonResponse({'ok': True, 'members':member_serializer.data}, safe=False)
