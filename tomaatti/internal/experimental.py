# Copyright (C) 2017 - 2018 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.


class ScreenOverlay(object):
	@staticmethod
	def is_coposite_manager_running():
		from subprocess import Popen, PIPE
		child = Popen(['pgrep', 'xcompmgr'], stdout=PIPE)
		child.communicate()
		if 0 == child.returncode:
			return True
		else:
			return False

	def __init__(self):
		self._tkinter_root = None
		self._overlay_canvas = None

	def show_overlay(self):
		from tkinter import Canvas, Tk

		self._tkinter_root = Tk()

		screen_width = self._tkinter_root.winfo_screenwidth()
		screen_height = self._tkinter_root.winfo_screenheight()

		self._overlay_canvas = Canvas(width=screen_width, height=screen_height, highlightthickness=0)
		self._overlay_canvas.configure(background='black')
		self._overlay_canvas.master.overrideredirect(True)
		self._overlay_canvas.master.geometry('+0+0')
		self._overlay_canvas.master.lift()
		self._overlay_canvas.master.wm_attributes('-topmost', True)
		self._overlay_canvas.master.wm_attributes('-fullscreen', True)
		self._overlay_canvas.master.wm_attributes('-zoomed', False)
		self._overlay_canvas.master.wm_attributes('-alpha', 0.5)
		self._overlay_canvas.create_rectangle(0, 0, screen_width, screen_height, fill='black')
		self._overlay_canvas.bind('<Button-1>', self._close_callback)
		self._overlay_canvas.pack()

		self._overlay_canvas.mainloop()

	def _close_callback(self):
		self._tkinter_root.destroy()
