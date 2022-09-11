from django.shortcuts import render, redirect

from main.forms import ProfileForm
from main.helpers import get_profile
from main.models import Pet, PetPhoto


def show_profile(request):
    profile = get_profile()
    pets = list(Pet.objects.filter(user_profile=profile))
    pet_photos = PetPhoto.objects \
        .filter(tagged_pets__in=pets) \
        .distinct()

    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_pet_photos_count = len(pet_photos)
    context = {
        'profile': get_profile(),
        'total_likes_count': total_likes_count,
        'total_pet_photos_count': total_pet_photos_count,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }

    return render(request, 'profile_create.html', context)


def edit_profile(request):
    return render(request, 'profile_edit.html')


def delete_profile(request):
    return render(request, 'profile_delete.html')
