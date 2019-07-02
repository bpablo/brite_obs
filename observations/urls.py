from django.urls import path
from . import views

urlpatterns = [
     path(r'obs_submission/', views.obs_submission.as_view()),
     path(r'observations/', views.Observations.as_view()),
     path(r'field/<int:fieldno>/<slug:fieldname>/', views.ObservationField.as_view()),
]
