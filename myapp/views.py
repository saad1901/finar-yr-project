from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import S3FileUploadForm
from .models import S3File

@login_required
def dashboard_view(request):
    files = S3File.objects.filter(user=request.user)
    return render(request, 'myapp/dashboard.html', {'files': files})

@login_required
def upload_file_view(request):
    if request.method == 'POST':
        form = S3FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            s3_file = form.save(commit=False)
            s3_file.user = request.user
            s3_file.file_name = request.FILES['file'].name
            s3_file.file_size = request.FILES['file'].size
            s3_file.save()
            messages.success(request, "File uploaded successfully.")
            return redirect('dashboard')
    else:
        form = S3FileUploadForm()
    
    return render(request, 'myapp/upload.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'myapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_file_view(request, file_id):
    s3_file = get_object_or_404(S3File, id=file_id, user=request.user) 
    if request.method == 'POST':
        s3_file.file.delete()  
        s3_file.delete()      
        messages.success(request, "File deleted successfully.")
        return redirect('dashboard')  
    return render(request, 'myapp/confirm_delete.html', {'file': s3_file}) 
