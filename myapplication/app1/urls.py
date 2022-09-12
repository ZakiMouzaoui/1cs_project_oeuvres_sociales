from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import ResetPasswordConfirmView

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('Employe', views.employe_view, name='Employe'),
    path('admin_', views.admin_program_view, name="admin_"),
    path('admin_crud', views.admin_crud_view, name="admin_crud"),
    path('partie_create', views.partie_create_view, name='partie_create'),
    path('partie_delete', views.partie_delete_view, name='partie_delete'),
    path('partie_update', views.partie_update_view, name='partie_update'),
    path('ajax_update_partie', views.partie_update_ajax_view, name='ajax_update_partie'),
    path('chapitre_create', views.chapitre_create_view, name='chapitre_create'),
    path('ajax_chapitre_create', views.create_chapitre_ajax, name='ajax_chapitre_create'),
    path('chapitre_update', views.chapitre_update_view, name='chapitre_update'),
    path('ajax_update_chapitre', views.chapitre_update_ajax_view, name='ajax_update_chapitre'),
    path('chapitre_delete', views.chapitre_delete_view, name='chapitre_delete'),
    path('article_create', views.article_create_view, name='article_create'),
    path('ajax_create_article', views.article_ajax_create_view, name='ajax_create_article'),
    path('article_update', views.article_update_view, name='article_update'),
    path('ajax_update_article', views.ajax_update_article_view, name='ajax_update_article'),
    path('article_delete', views.article_delete_view, name='article_delete'),
    path('upload', views.upload_file_view, name='upload'),
    path('demande/<int:article_id>', views.demande_view, name='demande'),
    path('search', views.search_view, name='search'),
    path('add_employee', views.add_employe_view, name='add_employee'),
    path('edit_employee/<int:employee_id>', views.edit_employee_view, name='edit_employee'),
    path('delete_employee/<int:employee_id>', views.delete_employe_view, name='delete_employee'),
    path('demandes', views.demande_list_view, name='demandes'),
    path('ajax_demande', views.ajax_demande_view, name='ajax_demande'),
    path('traiter_demande', views.traiter_demande_view, name='traiter_demande'),
    path('creer_pret', views.create_pret_view, name='creer_pret'),
    path('prets', views.pret_list_view, name='prets'),
    path('ajax_pret', views.ajax_pret_view, name='ajax_pret'),
    path('traiter_pret', views.traiter_pret_view, name='traiter_pret'),
    path('delete_multiple_employee', views.delete_multiple_employee_view),
    path('annonce', views.annonce_create_view, name='annonce'),
    path('ajax_update_annonce', views.ajax_update_annonce_view, name='ajax_update_annonce'),
    path('update_annonce', views.annonce_update_view, name='update_annonce'),
    path('delete_annonce', views.annonce_delete_view, name='delete_annonce'),
    path('annonce_inscription', views.annonce_inscription_view, name='annonce_inscription'),
    path('inscriptions', views.inscriptions_list_view, name='inscriptions'),
    path('accepter_inscription', views.accepter_inscription_view, name='accepter_inscription'),
    path('refuser_inscription', views.refuser_inscription_view, name='refuser_inscription'),
    path('ajouter_pv', views.pv_create_view, name='ajouter_pv'),
    path('pv_ajax', views.pv_ajax_view, name='pv_ajax'),
    path('modifier_pv', views.modifier_pv_view, name='modifier_pv'),
    path('supprimer_pv', views.supprimer_pv_view, name='supprimer_pv'),
    path('ajax_notification', views.notification_view, name='ajax_notification'),
    path('profile', views.user_profile_view, name='profile'),
    path('reset_password_view', views.reset_password_view, name='reset_password_view'),
    path('password_reset_done', views.password_reset_done_view, name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="app1/password_reset_complet.html"), name='password_reset_complete'),
    path('change_password', views.change_password_view, name='change_password'),
    path('ajax_update_image', views.change_image_view, name='ajax_update_image'),
    path('ajax_budget', views.ajax_budget_view, name='ajax_budget'),
    path('ajouter_budget', views.ajouter_budget_view, name='ajouter_budget'),
    path('ajouter_recette', views.ajouter_recette_view, name='ajouter_recette')
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""path("demande_create2", views.create, name="demande_create2"),
    path("uploads", views.send_files, name="uploads")"""