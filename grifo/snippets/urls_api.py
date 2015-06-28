from grifo.snippets import api
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'snippets', api.SnippetViewSet)

urlpatterns = router.urls