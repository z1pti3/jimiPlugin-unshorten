import jimi

class _unshorten(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("unshortenURL","_unshortenURL","_action","plugins.unshorten.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("unshortenURL","_unshortenURL","_action","plugins.unshorten.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        pass
        #if self.version < 0.2:
