
import subprocess
import os
import time

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(THIS_FOLDER, 'config.txt')

if __name__ == "__main__":
	print("EXECUTING...")

	# Reads the time set in config.txt
	file = open(FILE_PATH, "r")
	line = file.readline()
	sleep_time = int(line.split("=")[1]) * 60
	file.close();

	while (True):
		print ("Attempting to close Bluestacks...")
		subprocess.call(["taskkill", "/f", "/im", "BlueStacks.exe"]);
		time.sleep(3)
		
		print("Starting Bluestacks...")
		subprocess.call(["C:\\Program Files\\BlueStacks\\HD-RunApp.exe", "-json", "{\"app_icon_url\":\"\",\"app_name\":\"AFK Arena\",\"app_url\":\"\",\"app_pkg\":\"com.lilithgame.hgame.gp\"}"])
		time.sleep(sleep_time)
