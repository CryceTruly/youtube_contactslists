from django.urls import path
from .views import ContactListAPIView, ContactDetailAPIView

urlpatterns = [
    path('', ContactListAPIView.as_view()),
    path('<int:id>', ContactDetailAPIView.as_view()),
]
