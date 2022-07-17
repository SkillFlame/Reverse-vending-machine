# Main file

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from system import System
import settings


class IdleScreen(Screen):
	pass


class AppCouponScreen(Screen):
	pass


class QRCodeScreen(Screen):
	pass


class MainApp(App):
	def __init__(self, *args):
		self.system = System()
		super(MainApp, self).__init__()

	###########################################################################
	# UI functions
	###########################################################################

	def set_idle_screen(self, *args):
		self.stop_timers()
		self.sm.current = 'idle'
		self.create_new_system()

	def start_inactive_timer(self, *args):
		self.idle_event = Clock.schedule_once(
			self.set_idle_screen, settings.MAX_INACTIVE_TIME)

	def reset_inactive_timer(self, *args):
		self.stop_timers()
		self.start_inactive_timer()

	def start_qr_code_timer(self, *args):
		self.qr_code_event = Clock.schedule_interval(
			self.handle_app_selected, 1/60)

	def stop_timers(self, *args):
		Clock.unschedule(all)

	def build(self):
		Builder.load_file("ui.kv")
		self.sm = ScreenManager()
		self.sm.add_widget(IdleScreen())
		self.sm.add_widget(AppCouponScreen())
		self.sm.add_widget(QRCodeScreen())
		# Window.size = (1920, 1080)
		# Window.fullscreen = 'auto'
		return self.sm

	###########################################################################
	# System functions
	###########################################################################

	def create_new_system(self):
		'''
		Creates a new system
		'''
		self.system = System()

	###########################################################################
	# Main program functions
	###########################################################################

	def handle_app_selected(self, *args):
		'''
		Executes program functions necessary if app is chosen
		'''
		if(self.system.handle_qr_code_reading()):
			self.stop_timers()
			self.handle_program_cycle()

	def handle_program_cycle(self, *args):
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
		self.create_new_system()
		if(self.system.handle_bin_capacity()):
			self.display_full_bin_screen()


# Starts the UI
if __name__ == "__main__":
	MainApp().run()
