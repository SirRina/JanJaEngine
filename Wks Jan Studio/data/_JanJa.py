import ctypes
import math
import sys
import os

sys.path.insert(0, "{}\\SDL.dll".format(os.getcwd()))
sys.path.insert(0, "{}\\data\\func".format(os.getcwd()))

import json

class load(object):
	def __init__(self, path):
		try:
			self.path = open(path, "r+")
			self.file  = json.load(self.path)
		except:
			raise
		return None

	def set(self, item_json, write_json):
		try:
			self.file[item_json] = write_json
	
			self.path.seek(0)
			json.dump(self.file , self.path)
			self.path.truncate()
		except:
			raise
		return None

	def new(self, item_json, write_json):
		try:
			self.file[item_json] = write_json
	
			self.path.seek(0)
			json.dump(self.file , self.path)
			self.path.truncate()
		except:
			raise
		return None

	def rem(self, item_json):
		try:
			del self.file[item_json]
	
			self.path.seek(0)
			json.dump(self.file , self.path)
			self.path.truncate()
		except:
			raise
		return None

	def get(self, _value):
		try:
			return self.file[_value]
		except:
			raise
		return None

	def __repr__(self):
		try:
			return self.file
		except:
			raise
		return None

global JAN_ENGINE_path
global JAN_ENGINE_embed

JAN_ENGINE_path  = load("data/_np/JanEnginePath.json")

# Fix paths
JAN_ENGINE_path.new("Jan_Engine", "{}\\data\\_np\\JanEngine.json".format(os.getcwd()))

try:
	# pygame import
	from pygame import *
	import pygame
except:
	raise

global JAN_ENGINE_engine

JAN_ENGINE_engine = load(JAN_ENGINE_path.get("Jan_Engine"))

from JanFrame import *
from JAnGui   import *