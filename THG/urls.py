from django.urls import path
from . import views

urlpatterns = [
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('technology/',views.technology_posts, name="technology"),
    path('design/',views.design_posts, name="design"),
    path('database/',views.database_posts, name="database"),
    path('security/',views.security_posts, name="security"),
    path('hacking/',views.hacking_posts, name="hacking"),
    path('cybersecurity/',views.cybersecurity_posts, name="cybersecurity"),

    path('tech_quiz/', views.tech_quiz, name='tech_quiz'),
    path('design_quiz/', views.design_quiz, name='design_quiz'),
    path('db_quiz/', views.db_quiz, name='db_quiz'),
    path('security_quiz/', views.security_quiz, name='security_quiz'),
    path('hacking_quiz/', views.hacking_quiz, name='hacking_quiz'),
    path('cybersecurity_quiz/', views.cybersecurity_quiz, name='cybersecurity_quiz'),

    path('postComment', views.postComment, name="postComment"),
    path('textutils_tool/', views.textutils, name='textutils_tool'),
    path('analyze',views.analyze_text,name='analyze'),
    path('binary_text_converter/',views.binary_text_converter, name='binary_text_converter'),
    path('converting_text_binary',views.converting_text_binary, name='converting_text_binary'),
    path('password_generator_tool/', views.password_generate, name='password_generator_tool'),
    path('generated_password',views.password_generator, name='generated_password'),
    path('email_pwned_checker/',views.email_pwned_checker, name='email_pwned_checker'),
    path('privacy_policy_generator',views.privacy_policy_generator, name='privacy_policy_generator'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms_and_conditions', views.terms_and_conditions, name='terms_and_conditions'),
    path('text_to_speech', views.text_to_speech, name="text_to_speech"),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.HomeView.as_view(), name='home'),
    path('<str:slug>/', views.PostDetailView, name='post_detail'),
    path('search', views.search, name='search'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
]