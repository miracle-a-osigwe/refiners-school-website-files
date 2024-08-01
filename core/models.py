from django.db import models, connection
from django.core.validators import (
    MinValueValidator, MaxValueValidator
)
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.

class Section(models.Model):
    """The school sections"""
    section_dict = {
        1 : 'Pre-School', 
        2 : 'Primary',
        3 : 'Junior',
        4 : 'Senior'
        }
    
    sec_class = [
        (1, 'Pre-School'),
        (2, 'Primary'),
        (3, 'Junior'),
        (4, 'Senior')
    ]
    category = models.IntegerField(verbose_name='Category', choices=sec_class)

    def __str__(self):
        # result = "Junior" if self.category == 1 else "Senior"
        return str(self.section_dict.get(self.category, ' '))

class Subject(models.Model):
    """A Subject model to store subjects."""
    #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Section, verbose_name='Section', on_delete=models.CASCADE, related_name='section_subjects')
    name = models.CharField(verbose_name='Subject', max_length=30)
    
    def id(self):
        return self.id

    def subs(self, id):

        with connection.cursor() as cursor:
            cursor.execute("SELECT name from core.subject WHERE category = %d", [id])
            row = cursor.fetchall()
            return row
            
    def __str__(self):
        # result = "Junior" if self.category == 1 else "Senior"
        return  f"{str(self.name)} ({str(self.category)})"
    
    def junior_subjects():
        return Subject.objects.filter(Subject.category==1).all()

class Admin(models.Model):
    """
    Admin users, those who are neither students nor teachers but an admin of the school.
    """
    idx = models.OneToOneField(User, verbose_name='Registration number', on_delete=models.CASCADE, primary_key=True)
    admin_roles = [
        (1, 'Administrative'),
        (2, 'Management staff'),
        (3, 'Business owner')
    ]
    role = models.CharField(verbose_name='Admin role', choices=admin_roles, max_length=30)

    def __str__(self):
        return self.role

class Teacher(models.Model):

    """A Teacher model to reference from the User model."""
    
    # with connection.cursor() as cursor:
    #     cursor.execute
    #[(id, data) for id, data in enumerate(Subject().subs(category))]

    idx = models.OneToOneField(User, verbose_name='Registration number', on_delete=models.CASCADE, primary_key=True)
    subjects = models.ManyToManyField(Subject, verbose_name="Subject", related_name='+')
    # subject_class = models.

    def __str__(self):
        return str(self.idx)

class Class(models.Model):
    """Classes in the school"""
    
    name = models.CharField(verbose_name='Class name', max_length=30, unique=True)
    section = models.ForeignKey(Section, verbose_name='Section', on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, verbose_name='Teachers')
    subjects = models.ManyToManyField(Subject, verbose_name="Subjects", related_name='class_subjects')

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('mcq:detail', kwargs={'pk': self.pk})

class Student(models.Model):
    """A model class for students."""
    id = models.OneToOneField(User, verbose_name='Registration number', on_delete=models.CASCADE, primary_key=True)
    std_class = models.ForeignKey(Class, verbose_name='Class', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)


class Result(models.Model):
    """A result table to hold the values of each child."""
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    result = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

class Home(models.Model):
    """
    To keep the required data needed for the homepage.
    """
    author = models.CharField(max_length=3000)
    welcome = models.TextField(verbose_name='Homepage welcome address')

class SchoolVision(models.Model):
    """
    School vision, mission etc.
    """
    motto = models.CharField(max_length=50)
    vision = models.TextField(verbose_name='School vision')
    mission = models.TextField(verbose_name='School mission')
    creed = models.TextField(verbose_name='School creed')
    core_values = models.TextField(verbose_name='Core values')


class AboutUs(models.Model):
    """
    About Us record.
    """
    school_history = models.TextField(verbose_name='School History')
    school_owner_welcome_address = models.TextField(verbose_name='School Owner Welcome Address')
    school_vision_and_mission = models.ForeignKey(SchoolVision, on_delete=models.CASCADE)
    student_leadership = models.TextField()
    staff_report = models.TextField(verbose_name='Our Staff')
    result_report = models.TextField(verbose_name='Result and Honours Roll')

class CandidateInfo(models.Model):
    """
    Custom form for admission.
    """
    surname = models.CharField(verbose_name='Surname')
    firstName = models.CharField(verbose_name='First Name')
    address = models.CharField(verbose_name='Residential Address')
    dob = models.DateField(verbose_name='Date of Birth')
    origin = models.CharField(verbose_name='State of Origin')
    nationality = models.CharField(verbose_name='Nationality')
    religion = models.CharField(verbose_name='Religion')
    # age = models.IntegerField(verbose_name='Child\'s age')

    def __str__(self):
        return f"{self.surname}_{self.firstName}"
    
    class Meta:
        verbose_name = 'Candidate Information'
        verbose_name_plural = 'Candidates Information'

class CandidatePreviousSchool(models.Model):
    """
    Custom form for admission - Candidate Education Information.
    """
    candidate = models.ForeignKey(CandidateInfo, on_delete=models.CASCADE, related_name="candidate_previous_school")
    school_name = models.CharField(verbose_name='School name', blank=True)
    date_history = models.CharField(verbose_name='Date', blank=True)
    qualification = models.CharField(verbose_name='Qualification', blank=True)
    date_qualification = models.CharField(verbose_name='Date', blank=True)
    
    def __str__(self):
        return self.school_name
    
    class Meta:
        verbose_name = 'Candidate Previous School'
        verbose_name_plural = 'Candidates Previous Schools'

class ParentInfo(models.Model):
    """
    Custom form for admission - Parent Information.
    """
    candidate = models.ForeignKey(CandidateInfo, on_delete=models.CASCADE, related_name="candidate_parent")
    parent_surname = models.CharField(verbose_name='Parent Surname')
    parent_name = models.CharField(verbose_name='Parent First Name')
    home_address = models.CharField(verbose_name='Home Address')
    profession = models.CharField(verbose_name='Profession')
    office_address = models.CharField(verbose_name='Office Address')
    parent_religion = models.CharField(verbose_name='Religion')
    email_address = models.CharField(verbose_name='Email Address')
    relation = models.CharField(verbose_name='Relationship')
    contact_number = models.CharField(verbose_name='Contact Number', max_length=15)

    def __str__(self):
        return f"{self.parent_surname}_{self.parent_name}"

    class Meta:
        verbose_name = 'Parent Details'
        verbose_name_plural = 'Parents Details'