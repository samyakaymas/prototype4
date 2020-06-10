from django.forms import ModelForm
from django import forms
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget
class TheoryTagForm(ModelForm):
    class Meta:
        model=Theory
        exclude=["userId"]