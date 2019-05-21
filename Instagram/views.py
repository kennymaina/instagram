from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image, Profile
from. forms import UploadForm, ProfileEditForm, UserEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    images = Image.objects.all()
    profile = Profile.objects.all()

    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login')
def userspace(request):
    current_user = request.user
    images = Image.objects.all()
    profile = Profile.objects.all()
    return render(request, 'index.html', locals())

@login_required(login_url='/accounts/login')
def upload_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by  = current_user
            image.save()

            return redirect('welcome')
    else:
        form = UploadForm()
    return render(request, 'post.html', {'uploadform':form})


@login_required(login_url='/accounts/login')
def update_profile_form(request):
    current_user = request.user
    if request.method == 'POST':
        profile_edit_form = ProfileEditForm(request.POST, request.FILES)
        user_edit_form = UserEditForm(request.POST, request.FILES)
        if profile_edit_form.is_valid() and user_edit_form.is_valid():
            user_edit_form.save()
            profile = profile_edit_form.save(commit=False)
            profile.user= current_user
            profile.save()
            messages.info(request, 'Update Success!!')
            print(profile)
            return redirect('welcome')

    else:
        profile_edit_form = ProfileEditForm()
        user_edit_form = UserEditForm()

    return render(request, 'update_profile.html', {'prof_form': profile_edit_form, 'user_form': user_edit_form})
