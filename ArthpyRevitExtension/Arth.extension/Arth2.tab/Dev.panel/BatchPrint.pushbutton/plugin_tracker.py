import os
from pyrevit import revit
from pyrevit import HOST_APP
from Autodesk.Revit.UI import UIApplication
def get_current_plugin_info():
    try:
        # Get Revit application
        app = HOST_APP.app
        print("Username: {}".format(app.Username))
        print("Revit Version: {}".format(app.VersionName))

    except Exception as e:
        print("Error getting information: {}".format(str(e)))
