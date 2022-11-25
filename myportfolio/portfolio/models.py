from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

from phonenumber_field.modelfields import PhoneNumberField

import datetime


project_type_choices = (
    ("Side Project", "Side project"),
    ("Internship Project", "Internship project"),
    ("Work Project", "Work project"),
)



class Profile(models.Model):
    '''
    Model that represents my profile.
    '''

    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    biography = models.TextField(null=False, blank=False, max_length=200)
    birthday = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False)
    hobbies_description = models.TextField(null=False, blank=False, max_length=200)


    def __str__(self):
        '''
        Return de object string representation
        '''

        return f'Profile {self.id}: {self.first_name} {self.last_name}'


    def serialize(self):
        '''
        Return the object JSON/Dictionary representation
        '''

        return {

            "first_name": self.first_name,
            "last_name": self.last_name,
            "biography": self.biography,
            "birthday": self.birthday,
            "phone_number": "+" + str(self.phone_number.country_code) + " " + str(self.phone_number.national_number),
            "email": self.email,
            "hobbies_description": self.hobbies_description,

        }



class Experience(models.Model):
    '''
    Model that represents an experience in my software engineer career.
    '''

    title = models.CharField(null=False, blank=False, max_length=50)
    name = models.CharField(null=False, blank=False, max_length=50)
    start_date = models.DateField(null=False, blank=False, default=None)
    end_date = models.DateField(null=False, blank=False, default=None)
    description = models.TextField(null=False, blank=False, max_length=255)
    is_work = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        '''
        Return de object string representation
        '''

        return f'{self.title} in {self.name}'

    def serialize(self):
        '''
        Return the object JSON/Dictionary representation
        '''

        return {

            "title": self.title,
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "is_work": self.is_work

        }
    


class Technology(models.Model):
    '''
    Model that represents a technology
    '''

    name = models.CharField(null=False, blank=False, max_length=50)
    domination = models.PositiveIntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __str__(self):
        '''
        Return de object string representation
        '''
        
        return f'{self.name}'

    def serialize(self):
        '''
        Return the object JSON/Dictionary representation
        '''

        return {
            'name': self.name,
            'domination': self.domination,
        }



class Project(models.Model):
    '''
    Model that represents a side project.
    '''

    name = models.CharField(null=False, blank=False, max_length=50)
    description = models.CharField(null=False, blank=False, max_length=500)
    project_type = models.CharField(null=False, blank=False, max_length=20, choices=project_type_choices, default="Side project")
    technologies = models.ManyToManyField(Technology, related_name="projects")
    repository = models.URLField(blank=True)
    site = models.URLField(blank=True)

    def __str__(self):
        '''
        Return the object string representation
        '''

        return f'{self.name}'

    def serialize(self):
        '''
        Return the object JSON/Dictionary representation
        '''

        return {
            'name': self.name,
            'description': self.description,
            'project_type': self.project_type,
            'technologies': [technology.serialize() for technology in self.technologies.all()],
            'repository': self.repository,
            'site': self.site,
        }



class SoftSkill(models.Model):
    '''
    Model that represents a soft skill
    '''

    name = models.CharField(null=False, blank=False, max_length=50)
    description = models.CharField(null=False, blank=False, max_length=500)

    def __str__(self):
        '''
        Return the object string representation
        '''

        return f'{self.name}'

    def serialize(self):
        '''
        Return the object JSON/Dictionary representation
        '''

        return {
            'name': self.name,
            'description': self.description,
        }



class Email(models.Model):
    '''
    Model that represents a email sent to me
    '''

    subject = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False, max_length=200)

    def __str__(self):
        '''
        Return the object string representation
        '''

        return f'From: {self.email}'

    def serialize(self):
        '''
        Return the object JSON/Dictionary representation
        '''

        return {
            'subject': self.subject,
            'email': self.email,
            'message': self.message,
        }