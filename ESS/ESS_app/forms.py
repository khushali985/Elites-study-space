from django import forms 
from .models import StudyMaterial

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = [ 'branch', 'semester', 'material_type','subject_code', 'subject_name','file']