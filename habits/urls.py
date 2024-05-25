from habits.apps import HabitsConfig
from django.urls import path
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitPublicListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitPublicListAPIView.as_view(), name='habit_public' ),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('list/', HabitListAPIView.as_view(), name='habit_list'),
    path('view/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_view'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
