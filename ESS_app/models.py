from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary_storage.storage import RawMediaCloudinaryStorage

def custom_upload_path(instance, filename):
    branch = instance.branch.replace(" ", "_")
    subject_code = instance.subject_code.replace(" ", "_")
    return f"{branch}/Semester_{instance.semester}/{subject_code}/{filename}"

#model reprsenting study material databse
class StudyMaterial(models.Model):
    branch = models.CharField(max_length=100, verbose_name="Branch")
    semester = models.IntegerField(verbose_name="Semester")
    material_type = models.CharField(max_length=100, verbose_name="Materal Type")
    subject_code = models.CharField(max_length=50, verbose_name="Subject Code")
    subject_name = models.CharField(max_length=100, verbose_name="Subject Name")
    file = models.FileField(storage=RawMediaCloudinaryStorage(), upload_to=custom_upload_path, verbose_name="Upload File")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At")
    
    #ensure that the combination of subject_code and material_type is unique
    class Meta:
        unique_together = ( 'material_type', 'subject_code','subject_name')

    def _str_(self):
        return f"{self.branch} - {self.semester} - {self.subject_code} - {self.subject_name} - {self.material_type}"
    

# model for study_moment_gallery
class StudyMoment(models.Model):
    image = models.ImageField( storage=MediaCloudinaryStorage(), upload_to='study_moments/', verbose_name="Upload image")
    upload_at = models.DateTimeField( auto_now_add= True)
    
    def __str__(self):
        return f"Study Moment {self.id} - Uploaded at {self.upload_at}"
