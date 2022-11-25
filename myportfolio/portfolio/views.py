import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from .models import *


# Create your views here.
def index(request):

    profile = Profile.objects.first()

    return render(request, 'portfolio/index.html', {

        "profile": profile,

    })



def projects(request):

    template = 'portfolio/projects.html'

    if request.method == 'GET':
        
        try:

            # Get all project type objects
            projects = Project.objects.all()

        except:

            return render(request, template, {
                'error': 'Error 500: Can\'t access to projects in database',
            })

        return render(request, template, {
            'projects': projects,
        })

    else:
        
        return render(request, template, {
            'error': 'Error 405: The request method is not allowed',
        })



def cv(request):

    profile = Profile.objects.first()

    return render(request, 'portfolio/cv.html', {

        "profile": profile,

    })



def hire_me(request):
    return render(request, 'portfolio/hire_me.html')



# API Views

@csrf_exempt
def get_projects(request):
    '''
    Return all projects in the portfolio in JSON format
    '''

    if request.method == 'GET':
        
        try:

            # Get all project type objects
            projects = Project.objects.all()

        except:

            return JsonResponse({'error': 'Error 500: Cannot access to projects in database'}, status=500)

        data = {}

        if len(projects) == 0:

            data["alert"] = "There are not projects to show."

        else:

            for project in projects:
                data[f'{project.id}'] = project.serialize()

        data["status"] = 200

        return JsonResponse(data, status=200)

    else:
        return JsonResponse({'error': 'Error 405: the request method is not allowed'}, status=405)



@csrf_exempt
def get_soft_skills(request):
    '''
    Return all soft stkills objects
    '''

    if request.method == 'GET':

        try:

            # Get all soft skill objects
            soft_skills = SoftSkill.objects.all()

        except:

            return JsonResponse({'error': 'Error 500: Internal server error', "status": 500}, status=500)

        data = {}

        if len(soft_skills) == 0:

            data["alert"] = "There are not soft skills to show."

        else:

            for soft_skill in soft_skills:
                data[f'{soft_skill.id}'] = soft_skill.serialize()

        data["status"] = 200

        return JsonResponse(data, status=200)

    else:
        return JsonResponse({'error': 'Error 405: The request method is not allowed', "status": 405}, status=405)



@csrf_exempt
def get_experiences(request):
    ''''
    Return all experience objects
    '''

    if request.method == 'GET':

        try:

            experiences = Experience.objects.all()

        except:

            return JsonResponse({"error": "Error 500: Internal server error", "status": 500}, status=500)

        data = {}

        if len(experiences) == 0:

            data["alert"] = "There are not experience to show."

        else:

            for experience in experiences:
                data[f'{experience.id}'] = experience.serialize()

        data["status"] = 200

        return JsonResponse(data, status=200)

    else:
        
        return JsonResponse({'error': 'Error 405: The request method is not allowed', "status": 405}, status=405)



@csrf_exempt
def get_technologies(request):
    ''''
    Return all technologies objects
    '''

    if request.method == 'GET':

        try:

            technologies = Technology.objects.all().order_by('-domination')

        except:

            return JsonResponse({"message": "Error 500: Internal server error", "status": 500}, status=500)

        response = {}
        data = []

        if len(technologies) == 0:

            response["message"] = "There are not technologies to show."
            response["status"] = 200
            response["data"] = data
            response["alert"] = True

        else:

            for technology in technologies:
                data.append(technology.serialize()) 

            response["message"] = "Success"
            response["status"] = 200
            response["technologies"] = data

        return JsonResponse(response, status=200, safe=False)

    else:
        
        return JsonResponse({'message': 'Error 405: The request method is not allowed', "status": 405}, status=405)



@csrf_exempt
def profile(request):
    ''''
    Return profile info
    '''

    if request.method == 'GET':

        try:

            profile = Profile.objects.first()

        except:

            return JsonResponse({"message": "Error 204: There is not profile information", "status": 204}, status=204)

        data = {}

        if not profile:

            data["message"] = f'There is not a profile.'
            data["status"] = 200
            data["alert"] = True

        else:

            data["profile"] = profile.serialize()
            data["message"] = "Success"
            data["status"] = 200

        return JsonResponse(data, status=200, safe=False)

    else:
        
        return JsonResponse({'message': 'Error 405: The request method is not allowed', "status": 405}, status=405)


@csrf_exempt
def send_email(request):

    if request.method == 'POST':

        toEmails = ["jimenezwilliams.se@gmail.com"]

        data = json.loads(request.body)

        subject = data["subject"]
        fromEmail = data["email"]
        message = data["message"]

        try:

            email = Email(subject=subject, email=fromEmail, message=message)
            email.save()
            
        except:

            return JsonResponse({"message": "Error 500: Iternal server error", "status": 500}, status=500)

        send_mail(subject, f'From: {fromEmail}\nMessage: {message}', fromEmail, toEmails)

    else:

        return JsonResponse({"message": "Error 405: The request method is not allowed", "status": 405}, status=405)

    return JsonResponse({"message": "Thank you! Your mail has been sent successfully.",  "status": 201}, status=201)