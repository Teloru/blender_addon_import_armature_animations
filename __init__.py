

bl_info = {
    "name": "Import animated armature from Raymap",
    "author": "Spinu2b",
    "description": "This addon is supposed to import animated armature from Raymap tool - "
                   "level viewer/editor for Openspace games",
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

import bpy

from .addon_integration.create_animated_armature_op import CreateAnimatedArmatureOperator
from .addon_integration.addon_panel import AddonPanel, register_properties, unregister_properties

classes = (CreateAnimatedArmatureOperator, AddonPanel)

def register():
    register_properties()
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    unregister_properties()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
