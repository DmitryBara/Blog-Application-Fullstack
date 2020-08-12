from . import views
from django.urls import path

urlpatterns = [
	path('', views.all_articles, name = 'all_articles'),
	path('add_article/', views.add_article, name = 'add_article'),
	path('<int:article_id>/', views.one_article, name ='one_article'),
	path('edit_article/<int:article_id>', views.edit_article, name='edit_article'),
	path('change_visible/<int:article_id>', views.change_visible, name ='change_visible'),
	path('delete_article/<int:article_id>', views.delete_article, name='delete_article'),

	path('pa/my_articles/', views.my_articles, name = 'my_articles'),
]