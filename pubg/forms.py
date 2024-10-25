from django import forms


class StudentForm(forms.Form):
    school_name=forms.CharField(label="Name")
    school_place=forms.CharField(label="Place")
    about_school=forms.CharField()