from django.contrib import admin
from django.urls import path, include
from main.views import homeFeedView,leaderboardView
from pages.views import aboutPageView, searchView
from questions.views import (questionView, newView, answerView,
                            myQuestionsView, myAnswersView, questionVoteView,
                            answerVoteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # main app
    path('', homeFeedView),
    path('leaderboard/', leaderboardView),
    # pages
    path('search/', searchView, name='search'),
    path('about/', aboutPageView),
    # questions
    path('accounts/', include('allauth.urls')),
    path('question/<int:id>/', questionView),
    path('question/<int:id>/vote', questionVoteView),
    path('answer/<int:id>/vote', answerVoteView),
    path('question/<int:id>/answer', answerView),
    path('question/new/', newView),
    path('question/my_answers/', myAnswersView, name='my-answers'),
    path('question/my_questions/', myQuestionsView, name='my-questions'),
]
