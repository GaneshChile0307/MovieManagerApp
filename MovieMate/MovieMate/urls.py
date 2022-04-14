"""MovieMate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from MovieSet import login_register, user_side_apis , admin_side_apis 
from MovieSet import artist_data
from MovieSet import user_movie_track_data
from MovieSet import user_movie_rating_data
from MovieSet import sub_movie_rating_data
from MovieSet import sub_movie_data
from MovieSet import artist_type_data
from MovieSet import movie_category_data
from MovieSet import movie_data
from MovieSet import artist_movie_data


urlpatterns = [
    #Register and Login endpoints
    #path('admin/', admin.site.urls),
    path('register_user',login_register.register_user,name='register_user'),
    path('login_user',login_register.login_user,name='login_userp'),
    path('get_user_details_by_id/<int:user_id>' ,login_register.get_user_details_by_id,name='get_user_details_by_id'),
    path('get_user_details_by_email' ,login_register.get_user_details_by_email,name='get_user_details_by_email'),

    #Artist data endpoints
    path('add_artist',artist_data.add_artist,name='add_artist'),
    path('get_artist_details_by_id/<int:artist_id>' ,artist_data.get_artist_details_by_id,name='get_artist_details_by_id'),
    path('delete_artist',artist_data.delete_artist,name='delete_artist'),
    path('update_artist',artist_data.update_artist,name='update_artist'),
    path('get_all_artist_details',artist_data.get_all_artist_details,name='get_artist_details'),
    

    #user_movie_track_data
    path('add_movie_track_data',user_movie_track_data.add_movie_track_data,name='add_movie_track_data'),
    path('get_movie_track_data_by_id/<int:track_id>' ,user_movie_track_data.get_movie_track_data_by_id,name='get_movie_track_data_by_id'),
    path('delete_movie_track_data',user_movie_track_data.delete_movie_track_data,name='delete_movie_track_data'),
    path('update_movie_track_data',user_movie_track_data.update_movie_track_data,name='update_movie_track_data'),
    path('get_all_movie_track_data',user_movie_track_data.get_all_movie_track_data,name='get_all_movie_track_data'),


    #user_movie_rating_data
    path('add_movie_rating_data',user_movie_rating_data.add_movie_rating_data,name='add_movie_rating_data'),
    path('get_movie_rating_data_by_id/<int:rating_id>' ,user_movie_rating_data.get_movie_rating_data_by_id,name='get_movie_rating_data_by_id'),
    path('delete_movie_rating_data',user_movie_rating_data.delete_movie_rating_data,name='delete_movie_rating_data'),
    path('update_movie_rating_data',user_movie_rating_data.update_movie_rating_data,name='update_movie_rating_data'),
    path('get_all_movie_rating_data',user_movie_rating_data.get_all_movie_rating_data,name='get_all_movie_rating_data'),

    #sub_movie_rating_data
    path('add_sub_movie_rating_data',sub_movie_rating_data.add_sub_movie_rating_data,name='add_sub_movie_rating_data'),
    path('get_sub_movie_rating_data_by_id/<int:sub_movie_rating_id>' ,sub_movie_rating_data.get_sub_movie_rating_data_by_id,name='get_sub_movie_rating_data_by_id'),
    path('delete_sub_movie_rating_data',sub_movie_rating_data.delete_sub_movie_rating_data,name='delete_sub_movie_rating_data'),
    path('update_sub_movie_rating_data',sub_movie_rating_data.update_sub_movie_rating_data,name='update_sub_movie_rating_data'),
    path('get_all_sub_movie_rating_data',sub_movie_rating_data.get_all_sub_movie_rating_data,name='get_all_sub_movie_rating_data'),


    #sub_movie_data
     path('add_sub_movie_data',sub_movie_data.add_sub_movie_data,name='add_sub_movie_data'),
    path('get_sub_movie_data_by_id/<int:sub_movie_id>' ,sub_movie_data.get_sub_movie_data_by_id,name='get_sub_movie_data_by_id'),
    path('delete_sub_movie_data',sub_movie_data.delete_sub_movie_data,name='delete_sub_movie_data'),
    path('update_sub_movie_data',sub_movie_data.update_sub_movie_data,name='update_sub_movie_data'),
    path('get_all_sub_movie_data',sub_movie_data.get_all_sub_movie_data,name='get_all_sub_movie_data'),

     #artist type data endpoints
    path('get_artist_type_by_id/<int:artist_typeid>', artist_type_data.get_artist_type_by_id, name = 'get_artist_type_by_id'),
    path('get_artist_type', artist_type_data.get_artist_type, name = 'get_artist_type'),

    #movie category data endpoints
    path('get_movie_category_by_id/<int:moviecategoryid>', movie_category_data.get_movie_category_by_id, name = 'get_movie_category_by_id'),
    path('get_movie_category', movie_category_data.get_movie_category, name = 'get_movie_category'),

    #movie data endpoints
    path('add_movie',movie_data.add_movie,name='add_movie'),
    path('get_movie_data_by_id/<int:movieid>',movie_data.get_movie_data_by_id,name='get_movie_data_by_id'),
    path('delete_movie',movie_data.delete_movie,name='delete_movie'),
    path('update_movie',movie_data.update_movie,name='update_movie'),
    path('get_all_movie_data',movie_data.get_all_movie_data,name='get_all_movie_data'),

    #artist movie data endpoints 
    path('add_artist_movie',artist_movie_data.add_artist_movie,name='add_artist_movie'),
    path('get_artist_movie_data_by_id/<int:artist_movieid>',artist_movie_data.get_artist_movie_data_by_id,name='get_artist_movie_data_by_id'),
    path('delete_artist_movie',artist_movie_data.delete_artist_movie,name='delete_artist_movie'),
    path('update_artist_movie',artist_movie_data.update_artist_movie,name='update_artist_movie'),
    path('get_all_artist_movie_data',artist_movie_data.get_all_artist_movie_data,name='get_all_artist_movie_data'),

    #user side apis
    path('get_user_movie_track_data_by_userid/<int:user_id>',user_side_apis.get_user_movie_track_data_by_userid,name='get_user_movie_track_data_by_userid'),
    path('movie_not_watch_by_user/<int:user_id>',user_side_apis.movie_not_watch_by_user,name='movie_not_watch_by_user'),
    path('get_user_movie_rating_by_userid/<int:user_id>',user_side_apis.get_user_movie_rating_by_userid,name='get_user_movie_rating_by_userid'),
    path('no_movie_rating_by_userid/<int:user_id>',user_side_apis.no_movie_rating_by_userid,name='no_movie_rating_by_userid'),
    path('get_suggest_movies_userid',user_side_apis.get_suggest_movies_userid,name='get_suggest_movies_userid'),

    #admin side apis
    path('delete_artist_details_by_admin',admin_side_apis.delete_artist_details_by_admin,name='delete_artist_details_by_admin'),
    path('delete_movie_details_by_admin',admin_side_apis.delete_movie_details_by_admin,name='delete_movie_details_by_admin'),
    path('delete_sub_movie_details_by_admin',admin_side_apis.delete_sub_movie_details_by_admin,name='delete_movie_details_by_admin'),
]
