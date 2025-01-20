from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CardSet, Card
from .forms import CardSetForm, CardForm, ReviewForm

def home(request):
    card_sets = CardSet.objects.all()
    return render(request, 'cards/home.html', {'card_sets': card_sets})

def card_set_detail(request, pk):
    card_set = get_object_or_404(CardSet, pk=pk)
    return render(request, 'cards/card_set_detail.html', {'card_set': card_set})

def card_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    next_card = Card.objects.filter(id__gt=card.id, card_set=card.card_set).order_by('id').first()
    previous_card = Card.objects.filter(id__lt=card.id, card_set=card.card_set).order_by('-id').first()
    return render(request, 'cards/card_detail.html', {
        'card': card,
        'next_card': next_card,
        'previous_card': previous_card,
    })

@login_required
def card_set_create(request):
    if request.method == 'POST':
        form = CardSetForm(request.POST)
        if form.is_valid():
            card_set = form.save(commit=False)
            card_set.owner = request.user
            card_set.save()
            return redirect('home')
    else:
        form = CardSetForm()
    return render(request, 'cards/card_set_form.html', {'form': form})

@login_required
def card_set_edit(request, pk):
    card_set = get_object_or_404(CardSet, pk=pk)
    if card_set.owner != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = CardSetForm(request.POST, instance=card_set)
        if form.is_valid():
            form.save()
            return redirect('card_set_detail', pk=card_set.pk)
    else:
        form = CardSetForm(instance=card_set)
    return render(request, 'cards/card_set_form.html', {'form': form})

@login_required
def add_card(request, pk):
    card_set = get_object_or_404(CardSet, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.card_set = card_set
            card.save()
            return redirect('card_set_detail', pk=card_set.pk)
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form, 'card_set': card_set})

@login_required
def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_set_detail', pk=card.card_set.pk)
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/edit_card.html', {'form': form, 'card': card})

@login_required
def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card_set_id = card.card_set.pk
    card.delete()
    return redirect('card_set_detail', pk=card_set_id)

@login_required
def add_review(request, pk):
    card_set = get_object_or_404(CardSet, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.card_set = card_set
            review.user = request.user
            review.save()
            card_set.calculate_rating()
            return redirect('card_set_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'cards/add_review.html', {'form': form, 'card_set': card_set})


# urls.py (з папки без views)
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cards.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
