from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Form1ViewSet,Form2ViewSet,Form3ViewSet

router=DefaultRouter()
router.register('contact_api_a1',Form1ViewSet)
router.register('contact_api_a2',Form2ViewSet)
router.register('contact_api_a3',Form3ViewSet)


urlpatterns=[
    path('',include(router.urls))
    
]