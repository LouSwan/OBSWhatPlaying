from playsound import playsound as p
import time
import os
import random
import json

count = 0
current_status = "Waiting"
data = json.load(open('config.json'))
before = data['before']
after = data['after']

mode = str(input("Do you want the player to play randomly musics or left to right ? (default/random) ---> "))

def main():
	global current_status
	global mode
	mode = mode.lower()
	files = os.listdir()
	playlist = []
	files_time = []
	playing_files = ""
	for file in files:
		if ".mp3" in file:
			playlist.append(file)
			playing_files += file + " "
		elif ".ogg" in file:
			playlist.append(file)
			playing_files += file + " "
		elif ".mpeg" in file:
			playlist.append(file)
			playing_files += file + " "
		else:
			continue
	if len(playing_files) >= 1:
		print("The mp3 files in the directory are : " + playing_files)
	else:
		print("OOF There is not any mp3 file in that directory ! :(")
		return

	try:
		print("Playlist have " + str(len(playlist)) + " items ! ")
		time.sleep(0.5)
		while True:
			if mode == "default":
				for song in playlist:
					os.system('clear')
					playsound(song)
			elif mode == "random":
				os.system('clear')
				playsound(random.choice(playlist))
			else:
				print("[ERROR] The modes are random and default not {} !".format(mode))
				break
		with open("obs_read.txt", "w") as file:
			file.write("Currently playing NOTHING !")
	except FileNotFoundError:
		print("Cannot find this file !")
		main()
	quit = input("Press ENTER to exit the program !")

def playsound(url):
	global current_status
	global before
	global after
	current_status = "Playing"
	size_bytes = os.path.getsize(url)
	size = size_bytes / 1000
	print("The file size is " + str(size) + " kB !")
	current_path = os.getcwd()
	args = url.split(".")
	sound_name = args[0]
	print("Playing " + sound_name + " at " + current_path + "/" + url)
	print("STATUS : " + current_status, end='\r')
	with open("obs_read.txt", "w") as file:
		file.write(before + " " + args[0] + after)
	time.sleep(1)
	p(url)

main()
