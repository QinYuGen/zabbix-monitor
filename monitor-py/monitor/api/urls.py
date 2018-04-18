from django.conf.urls import url, include
from rest_framework import routers
import views
import agent_view

router = routers.DefaultRouter()
router.register(r'groups', views.GroupView, 'groups')
router.register(r'hosts', views.HostView, 'hosts')
router.register(r'cpu', views.CpuView, 'cpu')
router.register(r'memory', views.MemoryView, 'memory')
router.register(r'disk', views.DiskView, 'disk')
router.register(r'event', views.EventView, 'event')
router.register(r'usage', views.UsageView, 'usage')
router.register(r'totalUsage', views.TotalUsageView, 'totalUsage')
router.register(r'serviceItems', views.ServiceItemsView, 'service')
router.register(r'history', views.HistoryView, 'history')
router.register(r'template', views.TemplateView, 'template')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^deploy/', agent_view.deploy_agent, name='deploy'),
]
