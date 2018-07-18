from django import forms
from portal.models import Course,AllCourses



class add_course_form(forms.ModelForm):
    class Meta:
        model = AllCourses
        fields = '__all__'

class enroll_course_form(forms.Form):

    id = forms.IntegerField()
