import godot
from godot import Vector2, Input

@godot.expose_script_class
class PythonSprite(godot.Sprite2D, expose_all_methods=True):
	'''A simple script to demonstrate Python support.'''

	message: str = godot.property(default = 'hello world! 🐍