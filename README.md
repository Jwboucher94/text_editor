# text_editor
Python Text Editor
Version: 1.3

Welcome. This is a simple text editing program I'm working on in python. It's a relatively simple command line interface to use. As I think of them, I'll add more functionality. Functions are described below.

Main():
  Used to run the program. activates on start.

listDirectory(path_local, parent_local):
  Prints active path, parent path, and any folders in current path.
  If no folders exist, tells you.

pickDirectory(path_local, parent_local):
  Pulls global path and parent directories, and asks for a directory. listDirectory is run to show what directories are available. If you leave input blank, it will ask if finished. if you are finished, it will set global settings and continue on. if not, you will start over. if you type "..", it will go to the parent directory. it will only show the full path if you go up from the file's directory. If folder name does not exist, it will ask if you would like to create.

rawInput(text):
  used as an alternative in some cases to clear console. only used a few times because of other lines needing to be displayed. might deprecate.

job(response):
  determines which program to use based on response number. If you do not type a number between 1 and 5, it will give an error. program will not reach job if you type a letter.

fileNaming():
  lists all available files in current directory. if you do not type a file, it will try again.

finished():
  simple program that just asks if you are done. if you type anything with a y, the program will exit. otherwise, will return.

createFile(file_path, file_name):
  creates a file.

append(file_path, file_name):
  asks for input, opens the file (creates, if necessary) and creates a new line of text in file.

read(file_path, file_name):
  Will try to read the file asked for. if it does not exist, it will create.

question():
  manages asking which option to select. If your response is blank, it will ask if you are finished. if you do not type a number, it will give an error.

if __name__ == "__main__": starts main on start of program.
