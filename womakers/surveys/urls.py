# Docs
# - List View URL example: https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#listview
# - Detail View URL example: https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#detailview

from django.urls import path
from .views import QuestionListView, QuestionDetailView, VoteCreateView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
    path("<int:pk>/vote", VoteCreateView.as_view(), name="question-vote"),
]
