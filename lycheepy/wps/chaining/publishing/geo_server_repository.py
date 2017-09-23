from repository import Repository
from geoserver.catalog import Catalog
from lycheepy.settings import GEO_REPOSITORY_URL

WORKSPACE_NAME = 'lycheepy'


class GeoServerRepository(Repository):

    def __init__(self):
        super(GeoServerRepository, self).__init__()
        self.catalog = Catalog("{}geoserver/rest".format(GEO_REPOSITORY_URL))
        self.workspace = self.get_workspace()

    def get_workspace(self):
        workspace = self.catalog.get_workspace(WORKSPACE_NAME)
        if not workspace:
            workspace = self.catalog.create_workspace(WORKSPACE_NAME, WORKSPACE_NAME)
        return workspace

    def publish_raster(self, process, name, raster_file):
        self.catalog.create_coveragestore(name, raster_file, self.workspace, True)
        return '{}geoserver/wcs?SERVICE=WCS&REQUEST=GetCoverage&VERSION=2.0.1&CoverageId={}'.format(
            GEO_REPOSITORY_URL, name
        )

    def publish_features(self, process, name, features_file): raise NotImplementedError