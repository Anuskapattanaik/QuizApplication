from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Question, Score, UserProfile, CATEGORY_CHOICES
from .forms import UserForm, UserProfileForm

def home(request):
    categories = [cat[0] for cat in CATEGORY_CHOICES]
    return render(request, 'quiz_app/home.html', {'categories': categories})

@login_required(login_url='login')
def index(request, category):
    return render(request, 'quiz_app/index.html', {'category': category})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user) # Create empty profile
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'quiz_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz_app/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    # fallback for GET
    logout(request)
    return redirect('login')

def leaderboard(request):
    top_scores = Score.objects.select_related('user').order_by('-score', 'date_taken')[:10]
    return render(request, 'quiz_app/leaderboard.html', {'scores': top_scores})

def get_questions(request, category):
    questions_qs = Question.objects.filter(category=category).prefetch_related('options')
    quiz_data = []
    
    for q in questions_qs:
        options = []
        correct_index = -1
        
        for idx, opt in enumerate(q.options.all()):
            options.append(opt.text)
            if opt.is_correct:
                correct_index = idx
                
        quiz_data.append({
            'question': q.text,
            'options': options,
            'correctAnswer': correct_index
        })
        
    return JsonResponse(quiz_data, safe=False)

@login_required
def submit_score(request, category):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            score_val = data.get('score')
            if score_val is not None:
                Score.objects.create(user=request.user, category=category, score=score_val)
                return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def profile(request):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    # Calculate stats
    scores = Score.objects.filter(user=request.user)
    total_quizzes = scores.count()
    highest_score = scores.order_by('-score').first()
    
    stats_by_category = {}
    for score in scores:
        if score.category not in stats_by_category:
             stats_by_category[score.category] = {'count': 0, 'max': 0}
        stats_by_category[score.category]['count'] += 1
        stats_by_category[score.category]['max'] = max(stats_by_category[score.category]['max'], score.score)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'total_quizzes': total_quizzes,
        'highest_score': highest_score,
        'stats_by_category': stats_by_category
    }
    return render(request, 'quiz_app/profile.html', context)
