from django.conf.urls import patterns, url

from django.views.generic.base import TemplateView

from branch.views import CreateDemandView, CreateOfferView, CreateOfferObjView, CreateDemandObjView, \
                          DetailDemandView, DetailOfferView, DetailDemandObjView, DetailOfferObjView, \
                          UpdateDemandView, UpdateOfferView, UpdateOfferObjView, UpdateDemandObjView, \
                          CreateVolunteerView, ForceCreateVolunteerView, TakeOfferDemandView, CreateVolunteerObjView
                          
urlpatterns = patterns('',
# BEGIN|FRAMEWORK : OBJECTS
                       url(r'^new/demandObj/(?P<user_id>\d+)/$',
                           CreateDemandObjView.as_view(),
                           name='create_demandObj'),
                       url(r'^demandObj/(?P<demand_id>\d+)/$',
                           DetailDemandObjView.as_view(),
                           name='see_demandObj'),
                       url(r'^update/demandObj/(?P<demand_id>\d+)/$',
                           UpdateDemandObjView.as_view(),
                           name='update_demandObj'),
                       url(r'^delete/demandObj/(?P<demand_id>\d+)/$',
                           'branch.views.delete_demandObj',
                           name='delete_demandObj'),

                       url(r'^new/offerObj/(?P<user_id>\d+)/$',
                           CreateOfferObjView.as_view(),
                           name='create_offerObj'),
                       url(r'^offerObj/(?P<offer_id>\d+)/$',
                           DetailOfferObjView.as_view(),
                           name='see_offerObj'),
                       url(r'^update/offerObj/(?P<offer_id>\d+)/$',
                           UpdateOfferObjView.as_view(),
                           name='update_offerObj'),
                       url(r'^delete/offerObj/(?P<offer_id>\d+)/$',
                           'branch.views.delete_offerObj',
                           name='delete_offerObj'),
                       url(r'^volunteerObjD/(?P<volunteer_id>\d+)/demand/(?P<demand_id>\d+)/$',
                            CreateVolunteerObjView.as_view(),{'typeObj' : 1},
                            name='volunteer_objectD'),
                       url(r'^volunteerObjO/(?P<volunteer_id>\d+)/offer/(?P<demand_id>\d+)/$',
                            CreateVolunteerObjView.as_view(),{'typeObj' : 0},
                            name='volunteer_objectO'),
# END|FRAMEWORK : OBJECTS
                       url(r'^offer/(?P<user_id>\d+)/take/(?P<offer_id>\d+)/$',
                        TakeOfferDemandView.as_view(),
                        name='take_offer'),

                       url(r'^new/demand/(?P<user_id>\d+)/$',
                           CreateDemandView.as_view(),
                           name='create_demand'),
                       url(r'^update/demand/(?P<demand_id>\d+)/$',
                           UpdateDemandView.as_view(),
                           name='update_demand'),
                       url(r'^delete/demand/(?P<demand_id>\d+)/$',
                           'branch.views.delete_demand',
                           name='delete_demand'),
                       url(r'^delete/offer/(?P<offer_id>\d+)/$',
                           'branch.views.delete_offer',
                           name='delete_offer'),
                       url(r'^new/offer/(?P<user_id>\d+)/$',
                            CreateOfferView.as_view(),
                           name='create_offer'),
                       url(r'^update/offer/(?P<offer_id>\d+)/$',
                            UpdateOfferView.as_view(),
                           name='update_offer'),
                       url(r'^demand/(?P<demand_id>\d+)/$',
                            DetailDemandView.as_view(),
                           name='see_demand'),
                       url(r'^offer/(?P<offer_id>\d+)/$',
                            DetailOfferView.as_view(),
                           name='see_offer'),
                       # volunteer
                       url(r'^volunteer/(?P<volunteer_id>\d+)/demand/(?P<demand_id>\d+)/$',
                            CreateVolunteerView.as_view(),
                            name='volunteer_demand'),
 #                      url(r'^volunteer/forced/demand/(?P<demand_id>\d+)/$',
 #                           ForceCreateVolunteerView.as_view(),
 #                           name='force_volunteer_demand'),
                       # Stats
                       url(r'^statistics/(?P<user_id>\d+)/$',
                       'main.views.branch_statistics',
                       name='stats_branch'),
                       url(r'^branch_stats_reg_users_json/(?P<user_id>\d+)/$',
                       'main.views.get_branch_reg_users_json_view',
                       name='stats_branch_reg_users_json'),
                       url(r'^branch_stats_account_types_json/(?P<user_id>\d+)/$',
                       'main.views.get_branch_account_types_json_view',
                       name='stats_branch_account_types_json'),
                       url(r'^branch_stats_user_status_json/(?P<user_id>\d+)/$',
                       'main.views.get_branch_user_status_json_view',
                       name='stats_branch_user_status_json'),
                       url(r'^branch_stats_job_categories_json/(?P<user_id>\d+)/$',
                       'main.views.get_branch_job_categories_json_view',
                       name='stats_branch_job_categories_json')                      

                       )

