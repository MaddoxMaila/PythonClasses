
'''

Author : Tshepang Maddox Maila
Email : maddoxmaila719@gmail.com
Post : A Simple Music Application Created Using Python Tkinter With Pygame


'''
import tkinter as tk
import tkinter.filedialog as files
import pygame
import os

#Initialize The Tkinter Module
main = tk.Tk()

class MusicApp :

	def __init__(self,main) :
		self.main = main
		self.music_files = []
		#To hold position of the current playing song
		self.index = 1
		self.dir = ''
		#Button Declarations
		self.inputDirButton = tk.Button(self.main,text = 'Choose Directory',command=lambda:self.__ask_dir())
		self.inputDirButton.grid(row = 0,column = 0)
		self.PrevButton = tk.Button(self.main,text='Prev',command=lambda:self.__previous())
		self.PrevButton.grid(row = 0, column = 1)
		self.PlayButton = tk.Button(self.main,text='Play',command= lambda:self.__play(self.index))
		self.PlayButton.grid(row = 0, column = 2)
		self.NextButton = tk.Button(self.main,text='Next',command=lambda:self.__next())
		self.NextButton.grid(row = 0, column = 3)
		#End Of Button Declaration

	def __ask_dir(self) :
		#prompts the user to choose  directory to get music from
		self.dir = files.askdirectory()
		#change the working directory to user provided directory
		os.chdir(self.dir)
		self.__choose_music()
	def __choose_music(self) :
		#FOR LOOP TO Choose files
		x = 0
		for file in os.listdir(self.dir) :
			#only get files that of Audio Format
			if file.endswith('.mp3') or file.endswith('.flac') :
				self.music_files.append(os.path.realpath(file))
	def __play(self,index) :
		self.index = index
		try :
			#Using the pygame module to play music
			pygame.mixer.init()
			pygame.mixer.music.load(self.music_files[index])
			pygame.mixer.music.play()
		except :
			print('Error Playing This File ' + str(self.music_files[index]))

	def __next(self) :

		if self.index == len(self.music_files) :
			self.index = 0
			self.__play(self.index)
		else :
			self.index += 1
			self.__play(self.index)
	#DID NOT COVER THIS IN CLASS
	def __previous(self) :

		if self.index == 0 :
			#Set The Index To Play The Last Song
			self.index = len(self.music_files)
			self.__play(self.index)
		else :
			self.index -= 1
			self.__play(self.index)
	#END OF PREV
#Call Class Constructor
MusicApp(main)
print(dir(pygame.mixer.music))
main.mainloop()


'''
class Student :
    def __init__(maddox):
        maddox.stuName = ''
        maddox.stuEmail = ''
    def __set___(maddox,name,email):
        maddox.stuName = name
        maddox.stuEmail = email
    def __print__(maddox) :
        print(maddox.stuName)
        print(maddox.stuEmail)

student_one = Student()
student_one.__set___('Maddox','maddox@gmail')
#student_one.stuEmail = 'masfskjf@gmail.com'
#student_one.stuName = 'Tshepang'
student_one.__print__()
'''
