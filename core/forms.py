from django import forms
import pycountry
from .models import Teacher, Class, Student, Subject, CandidateInfo, CandidatePreviousSchool, ParentInfo

RELIGION = [('', 'Select Religion'), ('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Others', 'Others')]

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

class CandidateInfo(forms.ModelForm):
    """
    Custom form for admission.
    """
    class Meta:
        COUNTRIES = list(sorted((country.name, country.name) for country in pycountry.countries))
        COUNTRIES.insert(0, ('', 'Select Country'))
        model = CandidateInfo
        fields = ["surname", "firstName", "address", "dob", "origin", "nationality", "religion"]    
        widgets = {
            'surname': forms.TextInput(attrs={'placeholder': 'Enter your candidate\'s surname'}),
            'firstName': forms.TextInput(attrs={'placeholder': 'Enter your candidate\'s first name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter the home address'}),
            'dob': forms.TextInput(attrs={'placeholder': 'Enter the date attended', 'type':'date'}),
            'origin': forms.TextInput(attrs={'placeholder': 'Enter the state of origin'}),
            'nationality': forms.Select(choices=COUNTRIES),
            'religion': forms.Select(choices=RELIGION),
        }

class CandidatePreviousSchool(forms.ModelForm):
    """
    Custom form for admission - Candidate Education Information.
    """
    class Meta:
        model = CandidatePreviousSchool
        fields = ["school_name", "date_history", "qualification", "date_qualification"]
        widgets = {
            'school_name': forms.TextInput(attrs={
                'placeholder': 'Enter previous school name', 'blank':'true'}),
            'date_history': forms.TextInput(attrs={'placeholder': 'Enter the date attended', 'type':'date', 'blank':'true'}),
            'qualification': forms.TextInput(attrs={'placeholder': 'Any qualification(s) obtained', 'blank':'true'}),
            'date_qualification': forms.TextInput(attrs={'placeholder': 'Qualification issue date', 'type':'date', 'blank':'true'}),
        }

class ParentInfo(forms.ModelForm):
    """
    Custom form for admission - Parent Information.
    """
    class Meta:
        relationship = [('', 'Select Relationship'), ('Parents', 'Parents'), ('Guardian', 'Guardian')]
        model = ParentInfo
        fields = ["parent_surname", "parent_name", "home_address", "contact_number", "profession", 
                  "email_address", "office_address", "parent_religion", "relation"]
        widgets = {
            'parent_surname': forms.TextInput(attrs={'placeholder': 'Enter your surname'}),
            'parent_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'home_address': forms.TextInput(attrs={'placeholder': 'Enter your home address'}),
            'profession': forms.TextInput(attrs={'placeholder': 'Profession'}),
            'office_address': forms.TextInput(attrs={'placeholder': 'Office address'}),
            'parent_religion': forms.Select(choices=RELIGION),
            'relation': forms.Select(choices=relationship),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Contact number', 'type':'string'}),
            'email_address': forms.TextInput(attrs={'placeholder': 'Contact E-Mail'}),
        }
        
class EnquiryForm(forms.ModelForm):
    """
    Custom form for enquiry.
    """