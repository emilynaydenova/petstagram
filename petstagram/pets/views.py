# Create your views here.
from django.shortcuts import render, redirect

from pets.models import Pet, Like


def pet_all(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets
    }
    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    #  pet_likes_count = pet.like_set.count()
    # or monkey typing - add new attribute to pet
    pet.likes_count = pet.like_set.count()
    context = {
        'pet': pet,
        # 'pet_likes': pet_likes_count,
    }
    return render(request, 'pets/pet_detail.html', context)


def pet_likes(request, pk):
    # request.user -> who liked the pet
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet_to_like,
    )
    like.save()

    return redirect('pet details', pet_to_like.id)
