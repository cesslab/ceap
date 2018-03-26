from django.urls import path

app_name = 'experiments'

from .views import ExperimentListView

urlpatterns = [
    path('', ExperimentListView.as_view(), name='home')

]