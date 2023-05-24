from django.urls import path
from . import views

app_name = 'Movies'
# urlpatterns = [
#     path('actors/', views.actor_list),
#     path('actors/<int:actor_pk>/', views.actor_detail),
#     path('movies/', views.movie_list),
#     path('movies/<int:movie_pk>/', views.movie_detail),
#     path('movies/<int:movie_pk>/reviews/', views.create_review),
#     path('reviews/', views.review_list),
#     path('reviews/<int:review_pk>/', views.review_detail),
# ]

urlpatterns = [
    path('', views.movie_list),
    # path('', views.ApiTodoLV.as_view()),
    path('reviewlist/', views.review_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviewcreate/', views.review_create),
    path('<int:review_pk>/reviewdetail/', views.review_detail),
    path('<int:review_pk>/reviewdetail/comment/', views.review_comment),
    # path('<int:review_pk>/reviewdetail/commentlist/', views.comment_update_delete),
    path('<int:movie_id>/like/', views.movie_like),
]
