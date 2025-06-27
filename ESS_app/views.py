from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import StudyMaterial, StudyMoment
from .forms import StudyMaterialForm
from django.http import HttpResponse

# View for the home page
def Home_page(request):
    return render(request, 'Home_Page.html')


def file_not_available(request):
    return render(request, "file_not_available.html")


#View for the Civil_Engineering
def Civil_Engineering(request):
    files=StudyMaterial.objects.all()
    return render(request, 'Civil_Engineering.html', {'files': files})

#View for the Computer_Engineering
def Computer_Engineering(request):
    context = {'file': StudyMaterial.objects.all()}
    return render(request, 'Computer_Engineering.html', context)

#View for the Mechanical_Engineering
def Mechanical_Engineering(request):
    
    return render(request, 'Mechanical_Engineering.html')

# view for downloading functionality
def download_file(request,branch,semester, subject_code, subject_name, material_type):
    #Query the StudyMaterial model to get the correct study material
    study_material = get_object_or_404(
        StudyMaterial,
        branch=branch,
        semester=semester,
        subject_code=subject_code,
        subject_name=subject_name,
        material_type=material_type
    )
   # Redirect to the Cloudinary-hosted file
    if study_material.file:
        return redirect(study_material.file.url)
    else:
         return render(request, "file_not_available.html")
     
# view for the uploading the study material by the user
def upload_file(request):
    # If the request method is POST, it means the form is being submitted
    if upload_study_moment or request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        
        # Check if the form is valid
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('upload_success')  # Redirect to the upload success page
        else:
            print(form.errors)  # Print form validation errors for debugging
    
    # If the request method is GET, or after POST failure, render the form
    else:
        form = StudyMaterialForm()

    return render(request, 'Upload.html', {'form':form})


# view for the successful upload
def upload_success(request):
    return render(request, 'upload_success.html')

#view for downloading all the available files
def list_files(request):
    study_material= StudyMaterial.objects.all()
    return render(request, 'list_files.html', {'study_materials': study_material})

# view to show the gallery
def study_moment_gallery(request):
    # get all uploaded images from the database
    study_moments = StudyMoment.objects.all()
    return render(request, 'ESS_Moment_Gallery.html', {'study_moments': study_moments})

# view to hadale image upload
def upload_study_moment(request):
    if request.method == 'POST' and request.FILES('image'):
        image = request.FILES('image')
        study_moment = StudyMoment(image=image)
        study_moment.save() # save the uploaded image to the database
        return redirect('study_moment_gallery') # redirect to the gallery page
    
    return render(request, 'Home_page')

