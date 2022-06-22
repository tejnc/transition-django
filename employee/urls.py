from django.urls import path

from employee import views

urlpatterns = [
    path('employee/create/', views.EmployeeRegistrationAPIView.as_view()),
    path('employee/list/', views.EmployeeListAPIView.as_view()),
    path("notification/create/", views.NotificationCreateAPIView.as_view()),
    path("webhook/", views.WebhookReceivedAPIView.as_view())
]