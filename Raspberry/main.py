# Main file

from system import System


class Main():
	def __init__(self):
		self.system = System()
		
	###########################################################################
	# UI System functions
	###########################################################################

	def create_new_ui_system(self):
		'''
		Creates a new system
		'''
		self.system = System()

	###########################################################################
	# Main program functions
	###########################################################################

	def handle_app_selected(self):
		'''
		Executes program functions necessary if app is chosen
		'''
		self.display_scan_qr_screen()
		if(not self.system.handle_qr_code_reading()):
			self.display_app_coupon_screen()
		self.handle_program_cycle()

	def handle_program_cycle(self):
		'''
		Executes main program functions
		'''
		self.display_open_door_screen()
		if(self.system.handle_open_door()):
			self.system.handle_internal_light()
			if(not self.system.handle_object_detection()):
				self.display_insert_object_screen()
			if(not self.system.handle_close_door()):
				self.display.display_close_door_screen()
			self.display_processing_screen()
			self.system.handle_object_sorting()

		self.system.handle_points()
		self.system.handle_idle()
		self.display_idle_screen()
		self.create_new_ui_system()
		if(self.system.handle_bin_capacity()):
			self.display_full_bin_screen()


# Starts the UI
if __name__ == "__main__":
	pass
