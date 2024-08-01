from django import forms

from .models import Teacher, Class, Student, Subject

class TeacherForm(forms.ModelForm):
    """
    Custom Teacher Registration Form
    """
    pass

    # class Meta:
    #     model_name = Teacher
    #     fields = ('category', 'subjects')
    #     widgets = {
    #         'category': forms.CheckboxInput,
    #         'subjects': forms.CheckboxInput
    #     }

class CandidateInfo(forms.Form):
    """
    Custom form for admission.
    """
    surname = forms.CharField(label='Surname')
    firstName = forms.CharField(label='First Name')
    address = forms.CharField(label='Residential Address')
    dob = forms.DateField(label='Date of Birth', help_text="e.g. 4th, January 2023")
    origin = forms.CharField(label='State of Origin')
    nationality = forms.CharField(label='Nationality')
    religion = forms.CharField(label='Religion')
    # age = forms.IntegerField(label='Child\'s age')
    

class CandidatePreviousSchool(forms.Form):
    """
    Custom form for admission - Candidate Education Information.
    """
    history = forms.CharField(label='Previous School Attended')
    dates_history = forms.DateField(label='Dates')
    qualification = forms.CharField(label='Qualification Obtained')
    dates_qualification = forms.DateField(label='Dates')

class ParentInfo(forms.Form):
    """
    Custom form for admission - Parent Information.
    """
    parent_surname = forms.CharField(label='Parent Surname')
    parent_name = forms.CharField(label='Parent First Name')
    home_address = forms.CharField(label='Home Address')
    profession = forms.CharField(label='Profession')
    office_address = forms.CharField(label='Office Address')
    parent_religion = forms.CharField(label='Religion')
    email_address = forms.CharField(label='Email Address')
    relation = forms.CharField(label='Relationship to Candidate')
    contact_number = forms.IntegerField(label='Contact Number')




class EnquiryForm(forms.ModelForm):
    """
    Custom form for enquiry.
    """