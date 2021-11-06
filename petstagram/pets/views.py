# Create your views here.
from django.shortcuts import render, redirect

from common.forms import CommentForm
from common.models import Comment
from pets.forms import PetModelForm, PetEditForm
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
        'comment_form': CommentForm(),
        'comments': pet.comment_set.all(),
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


def pet_create(request):
    if request.method == 'GET':
        # show empty form
        form = PetModelForm()

    elif request.method == 'POST':
        # save form with the populated data
        form = PetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pets all', )

    context = {
        'form': form,
    }
    return render(request, "pets/pet_create.html", context)


def pet_edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = PetEditForm(instance=pet)

    elif request.method == 'POST':
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet details", pet.id)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, "pets/pet_edit.html", context)


def pet_delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':  # only 'Confirm' sends POST
        pet.delete()
        return redirect('pets all')
    else:  # GET is when Delete is choosen
        return render(request, "pets/pet_delete.html", {'pet': pet})


def add_comment(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = Comment(
            comment=form.cleaned_data['comment'],
            pet=pet,
        )
        new_comment.save()
    return redirect('pet details', pet.id)
