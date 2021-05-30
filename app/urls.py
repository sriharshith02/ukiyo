from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('feedback',views.feedback,name="feedback"),
    path('index',views.index,name="index"),
    path('overview',views.overview,name="overview"),
    path('Deppression',views.deppression,name="deppression"),
    path('Anger',views.anger,name="anger"),
    path('Anxiety',views.anxiety,name="anxiety"),
    path('Bullying',views.bullying,name="bullying"),
    path('Grief',views.grief,name="grief"),
    path('dashboard',views.dashboard,name="dashboard"),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)