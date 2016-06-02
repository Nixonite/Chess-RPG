import curses
import curses.textpad
import time


class Controller:
	
	def __init__(self, border_val = None):
		self._stdscr = curses.initscr()
		if border_val:
			self._stdscr.border(border_val)
		curses.noecho()
		curses.cbreak()
		self._stdscr.keypad(1)
		begin_x = 20
		begin_y = 7
		self._height = 15
		self._width = 60
		win = curses.newwin(self._height, self._width, begin_y, begin_x)
	
	def print_str(self, x, y, value):
		self._stdscr.addstr(y, x, value)
	
	def erase(self):
		self._stdscr.erase()
	
	def printc(self, value):
		self._stdscr.addstr(3, 3, value)
		self.refresh()
		self.waitKey()
		self.erase()
	
	def add_border(self, width):
		self._stdscr.border(1)
	
	def refresh(self):
		self._stdscr.refresh()
	
	def waitKey(self):
		self._stdscr.getch()
		
	def quit(self):
		curses.endwin()
