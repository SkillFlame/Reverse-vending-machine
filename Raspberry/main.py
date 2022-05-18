# Main file

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Dialog
from system import System


class Main():
	def __init__(self, ui):
		self.system = System()
		self.ui = ui

		#######################################################################
		# Ui Buttons
		#######################################################################

		# Button Idle
		self.ui.button_idle.clicked.connect(
			lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_app_coupon))

		# Button App
		self.ui.button_app.clicked.connect(
			lambda: self.handle_app_selected())

		# Button Coupon
		self.ui.button_coupon.clicked.connect(
			lambda: self.system.handle_open_door())

	###########################################################################
	# Switch UI screen functions
	###########################################################################

	def display_app_coupon_screen(self):
		'''
		Switches UI to app/coupon screen
		'''
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_app_coupon)

	def display_scan_qr_screen(self):
		'''
		Switches UI to scan QR code screen
		'''
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_scan_qr)

	def display_open_door_screen(self):
		'''
		Switches UI to open door screen
		'''
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_open_door)

	def display_insert_object_screen(self):
		'''
		Switches UI to insert object screen
		'''
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_insert_object)

	def display_close_door_screen(self):
		'''
		Switches UI to close door screen
		'''
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_close_door)

	def display_processing_screen(self):
		'''
		Switches UI to processing screen
		'''
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_processing)

	def display_idle_screen(self):
		'''
		Switches UI to idle screen
		'''
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_idle)

	def display_full_bin_screen(self):
		'''
		Switches UI to full recycling bin screen
		'''
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_full_bin)

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
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	gui = Main(ui)
	Dialog.show()
	sys.exit(app.exec_())
