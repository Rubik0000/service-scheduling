from django.shortcuts import render

# Create your views here.

from .models import RequestExercise, Trainer, ExerciseType


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_request_exercise = RequestExercise.objects.all().count()
    num_trainer = Trainer.objects.all().count()
    num_exercise_type = ExerciseType.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_request_exercise': num_request_exercise, 'num_trainer': num_trainer,
                 'num_exercise_type': num_exercise_type},
    )


from django.views import generic


class TrainerListView(generic.ListView):
    model = Trainer