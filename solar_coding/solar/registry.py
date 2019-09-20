"""

"""
class Registry:
    """
    Registry to hold objects, which can be utilized
    in flask app
    """
    obj = {}

    def __new__(cls, app, app_object):
        if app not in cls.obj:
            cls.obj[app] = app_object

    @classmethod
    def get(cls, app):
        return cls.obj[app]
