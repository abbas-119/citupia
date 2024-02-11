from django.urls import path, include
from . import views

app_name = 'home_page'
urlpatterns = [
    # path('', views.home_page, name='homePage'),
    # path('about/', views.about_page, name='aboutPage'),
    # path('contact/', views.contact_page, name='contactPage'),
    # path('faq/', views.faq_page, name='faqPage'),
    # path('privacy/', views.privacy_page, name='privacyPage'),
    # path('terms/', views.terms_page, name='termsPage'),
    path('user_prof/', views.UserProfileView.as_view()),
    path('geojson_data/', views.GeoJSONDataView.as_view()),
]