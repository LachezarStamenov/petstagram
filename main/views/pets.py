from django.shortcuts import render


def create_pet(request):
    return render(request, 'pet_create.html')


def edit_pet(request):
    return render(request, 'pet_create.html')


def delete_pet(request):
    return render(request, 'pet_delete.html')