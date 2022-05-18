# File for sensor handling

class Sensors():
	def __init__(self):
		self.user_id = None
		self.lights_on = False

	def read_qr_code(self):
		'''
		Reads T4G QR Code
		'''
		pass
		# FIXME Finish Function

	def get_user_id(self):
		'''
		Returns User id from QR Code
		'''
		return self.user_id

	def is_door_open(self):
		'''
		Checks if the machine door is open
		If is open returns, True
		Otherwise returns, False
		'''
		pass
		# FIXME Finish Function

	def is_lit(self):
		'''
		Checks ether there's enough light inside the machine
		If there's enough light returns, True
		Otherwise returns, False
		'''
		pass
		# FIXME Finish Function

	def toggle_lights(self):
		'''
		Toggles lights inside the machine
		If lights are off, turns on lights
		Otherwise, turns off lights
		'''
		pass
		# FIXME Finish Function

	def move_conveyor_belt(self, object_type):
		'''
		Moves conveyor belt
		Receives object type (plastic, tetrapack)
		Conveyor belt moves left if object is plastic/metal
		Conveyor belt moves right if object is tetrapack
		'''
		pass
		# FIXME Finish Function

	def print_coupon(self, object_type):
		'''
		Prints coupon with points
		Receives object type
		'''
		pass
		# FIXME Finish Function

	def get_bin_capacity(self):
		'''
		Returns Bin capacity [0, 100]
		'''
		pass
		# FIXME Finish Function
