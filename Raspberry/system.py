# File for system functions

import time

import settings

from sensors import Sensors
from computer_vision import ComputerVision
from database import DataBase
from notification import Notification

sensor = Sensors()


class System():

	def __init__(self):
		self.notification_sent = 0
		self.user_id = None
		self.objects = {'plastic': 0, 'tetrapack': 0}

	def handle_qr_code_reading(self):
		'''
		Handles QR code reading
		If is able to read QR code within a certain time period, returns True
		Otherwise, returns False
		'''
		if(sensor.read_qr_code()):
			self.user_id = sensor.get_user_id()
			return True
		return False

	def handle_open_door(self):
		# FIXME description
		'''
		Handles time for object input
		If door is open within a certain time period, returns True
		Otherwise, returns False
		'''
		must_end = time.time() + settings.MAX_OBJECT_WAITING_TIME
		while(time.time() < must_end):
			if(sensor.is_door_open()):
				return True

			time.sleep(settings.SLEEP_TIME)
		return False

	def handle_internal_light(self):
		'''
		Handles machine's internal lights
		If there's not enough light, turns on lights
		Otherwise, does nothing
		'''
		if(not sensor.is_lit):
			sensor.toggle_lights()

	def handle_object_detection(self):
		'''
		Handles object detection
		If an object is detected, returns True
		Otherwise, returns False
		'''
		# FIXME fix function
		return ComputerVision.is_object_detected()

	def handle_close_door(self):
		'''
		Handles closing of the door
		If door is closed, returns True
		Otherwise, returns False
		'''
		# FIXME fix function
		return sensor.is_door_open()

	def handle_object_sorting(self):
		'''
		Handles object sorting and Stores object time for point calculation
		'''
		object_type = ComputerVision.get_object_type()
		sensor.move_conveyor_belt(object_type)
		self.objects[object_type] += 1

	def handle_points(self):
		'''
		Handles points
		If App was selected, sends data to T4G database
		Otherwise, prints coupon
		'''
		# FIXME add point calculation
		if(self.user_id):
			DataBase.send_T4G_data(self.user_id, object_type)
		sensor.print_coupon(object_type)

	def handle_idle(self):
		'''
		Handles idle
		Turns of everything not needed
		'''
		pass
		# FIXME turn off everything not needed

	def handle_bin_capacity(self):
		'''
		Handles recycling bin capacity
		If bin capacity => threshold, sends notification
		If bin capacity == max capacity, displays bin full screen and locks machine
		Otherwise, does nothing
		'''
		bin_capacity = sensor.get_bin_capacity()

		if(bin_capacity < settings.THRESHOLD_BIN_CAPACITY):
			self.notification_sent = 0
			return
		if(bin_capacity == settings.MAX_BIN_CAPACITY):
			full_cycle()
			return True
		if(self.notification_sent):
			return

		Notification.send_full_notification()
		self.notification_sent = 1
