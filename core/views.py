from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from .models import Teacher, Student, Home, AboutUs, CandidateInfo, CandidatePreviousSchool, ParentInfo
from . import forms
from post.models import Post, UpdateImage, get_post
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from random import choice

# Create your views here.

#set app name
app_name = 'core'

# constants calling a function
IMAGES = None

def reload_images():
    global IMAGES
    IMAGES = UpdateImage.objects.filter(published=True).exclude(img_use='homepage')

class IndexView(TemplateView):
    template_name = 'core/home.html'
    # model = Home

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        offer_tag = get_post('offer')
        event_tag = get_post('event')
        mission_tag = get_post('mission')
        vision_tag = get_post('vision')

        context = super().get_context_data(**kwargs)
        
        context['about_us'] = Post.objects.filter(published=True).filter(post_category=1).order_by('-date_published').first()
        context['offer'] = self.sort_offer(Post.objects.filter(published=True).filter(post_category=offer_tag)) #.order_by('-date_published')
        context['event'] = Post.objects.filter(published=True).filter(post_category=event_tag).order_by('-date_published').first()
        context['mission'] = Post.objects.filter(published=True).filter(post_category=mission_tag).order_by('-date_published').first()
        context['vision'] = Post.objects.filter(published=True).filter(post_category=vision_tag).order_by('-date_published').first()

        images = UpdateImage.objects.filter(img_use="homepage").filter(published=True)
        images = create_pairs(images)
        media_url = settings.MEDIA_URL

        if images:
            context['homepage_images'] = images
        context['media_url'] = media_url.replace('/', '')
        context['popup'] = UpdateImage.objects.filter(img_use="others").filter(published=True).order_by('-date_published').first()
        return context
    
    def sort_offer(self, data):
        """
        A function to ensure that random data are returned per time
        """
        new_data = []
        creche, primary, nursery, secondary = [], [], [], []
        for item in data:
            if 'che' in item.title.lower():
                creche.append(item)
            elif 'nur' in item.title.lower():
                nursery.append(item)
            elif 'pri' in item.title.lower():
                primary.append(item)
            elif 'sec' in item.title.lower():
                secondary.append(item)
            else:
                pass
        # Use a for loop to select the variabel and then randomly pick the item to show.
        for item in [creche, primary, nursery, secondary]:
            new_data.append(choice(item))
        return new_data
        
class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['about_us_data_all'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=5)) #.order_by('-data_published').first()
        context['mission'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=2).first()) #.order_by('-data_published')
        context['vision'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=3).first()) #.order_by('-date_published')
        context['core_values'] = self.sort_core_values(Post.objects.filter(published=True).filter(post_category=8).first())
        context['school_anthem'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=9).first())
        context['school_creed'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=7).first())
        context['school_responsibility_pledge'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=10).first())
        return context
    
    def sort_core_values(self, text):
        if text:
            text.content = text.content.replace('\r\n', '\n').split('\n')
            text.content = [x.strip() for x in text.content]
        return text
    
    def sort_data(self, text):
        if isinstance(text, QuerySet):
            if text is not None:
                for txt in text:
                    txt.content = txt.content.replace('\r\n', ' <br> ')
                    if 'refine' in str(txt.content).lower():
                        txt.content = txt.content.replace('REFINERS', '<strong>REFINERS</strong>').replace('Refiners', '<strong>Refiners</strong>') 
            return text
        
        if text is not None:
            text.content = text.content.replace('\r\n', ' <br> ')
            if 'refine' in str(text.content).lower():
                text.content = text.content.replace('REFINERS', '<strong>REFINERS</strong>') 
            return text
        return None

class AdmissionView(TemplateView):
    template_name = 'core/admission.html'

def admit(request):
    if request.method == 'POST':
        form1 = CandidateInfo(request.POST)
        form2 = CandidatePreviousSchool(request.POST)
        form3 = ParentInfo(request.POST)
        if (form1.is_valid and form2.is_valid and form3.is_valid):
            form1.full_clean()
            form2.full_clean()
            form3.full_clean()
            print(form1.cleaned_data)
            print(request.POST)
            return render(request, 'core/home.html', {'message':'Form submitted successfully'})
        else:
            return render(request, 'core/admission.html', {"form1":form1, "form2":form2, "form3":form3})
    else:
        return render(request, 'core/admission.html', {"form1":forms.CandidateInfo, "form2":forms.CandidatePreviousSchool, "form3":forms.ParentInfo})

class MissionVisionView(TemplateView):
    template_name = 'core/mission_vision.html'

class GalleryView(TemplateView):
    template_name = 'core/gallery.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        reload_images()
        images = IMAGES
        context['event_images'] = self.sort_images(images, 'events')

        media_url = settings.MEDIA_URL
        context['media_url'] = media_url.replace('/', '')
        # print(context)
        return context
    
    def sort_images(self, images, category="homepage"):
        """
        Sorting functions for images
        """
        def sorter(category):
            data = []
            for image in images:
                if image.img_use == category:
                    data.append(image)
            return data
        
        return sorter(category)
        
            

class NewsView(TemplateView):
    template_name = 'core/news.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        # Get all the events
        event_tag = get_post('event')
        context['events'] = Post.objects.filter(published=True).filter(post_category=event_tag).order_by('-date_published')

        return context
    
class AlumniView(TemplateView):
    template_name = 'core/alumni.html'

class ResourcesView(TemplateView):
    template_name = 'core/resources.html'

class AcademicView(TemplateView):
    template_name = 'core/academics.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['academic_creche'] = self.sort_all(Post.objects.filter(published=True).filter(post_category=11))#.order_by('-data_published')
        context['academic_nursery'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=12).first())#.order_by('-data_published')
        context['academic_primary'] = self.sort_primary(Post.objects.filter(published=True).filter(post_category=13))#.order_by('-data_published')
        context['academic_junior'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=14).first())#.order_by('-data_published')
        context['academic_senior'] = self.sort_all(Post.objects.filter(published=True).filter(post_category=15))#.order_by('-data_published').first()

        return context
    
    def sort_primary(self, data):
        data = self.sort_all(data)
        upper = [d.content for d in data if 'general' in d.title.lower()][0]
        lower = upper[:]
        for d in data:
            d.title = d.title.lower()
            if 'lower' in d.title:
                lower.extend(d.content)
                d.content = lower
            elif 'upper' in d.title:
                upper.extend(d.content)
                d.content = upper

        return data
        
    
    def sort_data(self, text):
        if text:
            text.content = text.content.replace('\r\n', '\n').split('\n')
            text.content = [x.strip() for x in text.content]
        return text

    def sort_all(self, data):
        if data:
            for col in data:
                col = self.sort_data(col)
                col.title = col.title.lower()
        return data

class StudentView(generic.DetailView):
    template_name = 'core/student.html'
    model = Student

class FacilityView(TemplateView):
    template_name = 'core/facilities.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        reload_images()
        images = IMAGES
        labs = self.sort_images(images, 'labs')
        workshop = self.sort_images(images, 'workshops')
        context['labs_images'] = labs + workshop
        context['sports_images'] = self.sort_images(images, 'sports')
        context['building'] = self.sort_images(images, 'school_building')

        media_url = settings.MEDIA_URL
        context['media_url'] = media_url.replace('/', '')
        # print(context)
        return context
    
    def sort_images(self, images, category="homepage"):
        """
        Sorting functions for images
        """
        def sorter(category):
            data = []
            for image in images:
                if image.img_use == category:
                    data.append(image)
            return data
        
        return sorter(category)

class StaffView(generic.DetailView):
    model = Teacher
    template_name = 'core/staff.html'

    def get_queryset(self):
        return Teacher.objects.filter()

def create_pairs(lst):
    pairs = []
    for i in range(0, len(lst), 2):
        if i+1 < len(lst):
            pairs.append((lst[i], lst[i+1]))
        else:
            pairs.append((lst[i], None))  # Handling odd length lists
    return pairs

# @csrf_exempt
def submit_form(request):
    if request.method == "POST":
        candidate_form = forms.CandidateInfo(request.POST)
        candidate_history_form = forms.CandidatePreviousSchool(request.POST)
        parent_form = forms.ParentInfo(request.POST)

        if candidate_form.is_valid() and candidate_history_form.is_valid() and parent_form.is_valid():
            candidate = candidate_form.save()
            previous_school = candidate_history_form.save(commit=False)
            previous_school.candidate = candidate
            previous_school.save()
            parent = parent_form.save(commit=False)
            parent.candidate = candidate
            parent.save()

            # return JsonResponse({'status': 'success', 'message':'Form submitted successfully, Thank you for making this request'})
            # print("Succeed")
            return render(request, 'core/admission.html', {
                "candidate_form" : forms.CandidateInfo(), 
                "candidate_previous_school" : forms.CandidatePreviousSchool(), 
                "parent_form" : forms.ParentInfo(),
                'message':'Form submitted successfully, we will contact you shortly...'})
        
        else:
            # print(candidate_form.errors, candidate_history_form.errors, parent_form.errors)
            return render(request, 'core/admission.html', {
                "candidate_form" : candidate_form, 
                "candidate_previous_school" : candidate_history_form, 
                "parent_form" : parent_form,
                'errors': (candidate_form.errors, candidate_history_form.errors, parent_form.errors)})
            return JsonResponse({'status': 'failed', 'errors': (candidate_form.errors, candidate_history_form.errors, parent_form.errors)}, status=400)
    else:
        # print(request)
        candidate_form = forms.CandidateInfo()
        candidate_history_form = forms.CandidatePreviousSchool()
        parent_form = forms.ParentInfo()

        return render(request, 'core/admission.html', 
                      {"candidate_form" : candidate_form, 
                       "candidate_previous_school" : candidate_history_form, 
                       "parent_form" : parent_form})