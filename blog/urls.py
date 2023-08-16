from django.urls import path
from .views import render_posts, post_detail
from blog import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name="posts"),
    path("<int:post_id>", post_detail, name="post_detail"),
    path("<int:post_id>", views.PostView.as_view(), name="post_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)