def classFactory(iface):
    from .main_plugin import VerifPlugin
    return VerifPlugin(iface)
