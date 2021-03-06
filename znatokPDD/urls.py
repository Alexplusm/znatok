"""znatokPDD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from accounts import views
from django.contrib.auth import views as auth_views
from exam import views as exam_views
from game import views as game_views
from comments import views as comments_views
from online_game import views as online_game_views
from accounts import views as account_views

from django.views.generic import TemplateView

# from online_game import urls

urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(template_name='home.html'), name='home'),
    url(r'^ourteam', TemplateView.as_view(template_name='our_team.html'), name='our_team'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^confirm/$', TemplateView.as_view(template_name='confirm_email.html'), name='confirm'),
    url(r'^confirm/done', auth_views.LoginView.as_view(template_name='confirm_done.html'), name='confirm_done'),
    url(r'^confirm/fail', TemplateView.as_view(template_name='confirm_fail.html'), name='confirm_fail'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    url(r'^admin/', admin.site.urls),


    # urls for exam app

        # for ajax query
    url(r'load_ticket/$', exam_views.load_ticket, name='load_ticket'),
    url(r'load_question/$', exam_views.load_question, name='load_question'),
    url(r'check_answer/$', exam_views.check_answer, name='check_answer'),
    url(r'check_points/$', exam_views.check_points, name='check_points'),
    url(r'check_results/$', exam_views.check_results, name='check_results'),
    url(r'get_wrong_questions/$', exam_views.get_wrong_questions, name='get_wrong_questions'),
    url(r'load_questions_by_theme/$', exam_views.load_questions_by_theme, name='load_questions_by_theme'),

    url(r'load_picture/$', game_views.load_picture, name='load_picture'),
    url(r'next_mini_game/$', game_views.next_mini_game, name='next_mini_game'),
    url(r'reload_mini_game/$', game_views.reload_mini_game, name='reload_mini_game'),
    url(r'skip_mini_game/$', game_views.skip_mini_game, name='skip_mini_game'),
    url(r'check_answer_for_game/$', game_views.check_answer_for_game, name='check_answer_for_game'),
    url(r'check_game_is_ready/$', game_views.game_is_ready, name='game_is_ready'),

    url(r'get_comments/$', comments_views.load_comments, name='get_comments'),
    url(r'add_comments/$', comments_views.add_comments, name='add_comments'),
    url(r'get_leaders/$', comments_views.get_leaders, name='get_leaders'),
    url(r'get_more_comments/$', comments_views.get_more_comments, name='get_more_comments'),

    url(r'take_point/$', account_views.take_point, name='take_point'),

    url(r'get_block_achievement/$', account_views.get_block_achievement, name='get_block_achievement'),
    url(r'get_block_information/$', account_views.get_block_information, name='get_block_information'),

    url(r'get_block_theory_pdd/$', exam_views.get_block_theory_pdd, name='get_block_theory_pdd'),
    url(r'get_block_theory_inside', exam_views.get_block_theory_inside, name='get_block_theory_inside'),

    # urls for exam app

    # urls for online_game app
    url(r'^get_statistic/', online_game_views.get_statistic, name='get_statistic'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

