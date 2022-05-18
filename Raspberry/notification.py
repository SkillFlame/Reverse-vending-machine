# File for notification sending

import yagmail

import settings


class Notification():

	def send_full_notification():
		'''
		Sends notification that the bin is full
		'''
		header = "Yagmail test with attachment"
		body = "Hello there from Yagmail"
		filename = "document.pdf"

		yag = yagmail.SMTP("my@gmail.com")
		yag.send(
			to=RECEIVER_EMAIL,
			subject=header,
			contents=body,
			attachments=filename,
		)
