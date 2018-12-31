import os
if os.name == "posix":
	clear = "clear"
elif os.name == "nt":
	clear = "cls"
optargs = [
	"1. Create File",
	"2. Append File",
	"3. Read File",
	"4. Change Directory",
	"5. List directory"];
argcount = "1-"+str(len(optargs));
path = "./";
parent = (os.path.split(os.path.abspath("./"))[0]+"/");

def main():
	on = 1; #used for while loop
	os.system(clear);
	print(
		"Project: Text Modifier\n"
		"Version: 1.3\n"
		"Welcome. This is a side project to practice python coding. "
		"Enjoy!");
	raw_input("Press enter to start...");
	#following is used to list and determine directory folder and set path
	global path;
	global parent;
	print(pickDirectory(path, parent));
	#main while loop follows
	while on > 0:
		#ask which option to use
		response = question();
		job(response);

def listDirectory(path_local, parent_local):
	print("Current Path: " + path_local);
	print("Parent Path: " + parent_local);
	walk = next(os.walk(path_local))[1];
	if len(walk) == 0:
		print("No folders in current path!");
	else:
		for folder in walk:
			print ("- " + folder);
	print("- ..");

def pickDirectory(path_local, parent_local):
	global path;
	global parent;
	os.system(clear);
	print("Where shall we manage your files?");
	listDirectory(path_local, parent_local);
	folder = raw_input("Enter name of Directory (Use '..' to go back):\n>> ");
	if len(folder) == 0:
		answer = rawInput(
			"This is your path: " + path_local + ".\n"
			"Any changes? (n/y)\n>>");
		if answer == "y":
			pickDirectory(path_local, parent_local);
		else:
			path = path_local;
			parent = parent_local;
	elif folder == "..":
		if path_local == "//":
			pickDirectory(path, parent);
		else:
			if parent == "./":
				path = "./";
				parent = (os.path.split(os.path.abspath("./"))[0]+"/");
			else:
				path = parent;
				parent = (os.path.split(os.path.split(path)[0]))[0]+"/";
			pickDirectory(path, parent);
	else:
		path_new = (path_local + folder + "/");
		if not os.path.exists(path_new):
			answer = rawInput("Folder does not exist. Create? (y/n)\n>>")
			if answer == "n":
				path = path_local;
				parent = parent_local;
				pickDirectory(path, parent);
			else:
				os.makedirs(path_new);
		answer = rawInput(
			"This is your path: " + path_new + ".\n"
			"Any changes? (n/y)\n>>");
		if answer == "y":
			if path_new == (os.path.abspath("./")+"/"):
				path = "./";
				parent = (os.path.split(os.path.abspath("./"))[0]+"/");
			else:
				path = path_new;
				parent = path_local;
			pickDirectory(path, parent);
		else:
			path = path_new;
			parent = path_local;

def rawInput(text):
	os.system(clear);
	text = raw_input(text);
	return text;

def job(response):
	global path;
	global parent;
	if response == 1:
		file_path, file_name = fileNaming();
		createFile(file_path, file_name);
		finished();
		return;
	if response == 2:
		file_path, file_name = fileNaming();
		append(file_path, file_name);
		finished();
		return;
	if response == 3:
		file_path, file_name = fileNaming();
		read(file_path, file_name);
		finished();
		return;
	if response == 4:
		pickDirectory(path, parent);
		finished();
		return;
	if response == 5:
		listDirectory(path, parent);
		finished();
		return;
	else:
		rawInput(
			"Error: Options are " + argcount + ". "
			"\nPress enter to continue...");
		return;

def fileNaming():
	os.system(clear);
	print ("Available files:");
	for files in next(os.walk(path))[2]:
		print("- "+str(os.path.splitext(files)[0]));
	print("");
	file_name = str(raw_input("Please enter file name: \n>> "))
	file_path = path + file_name
	if len(file_name) == 0:
		print("Please enter a file name");
		fileNaming();
	return file_path, file_name

def finished():
 	response = raw_input("Are you finished? (y/n)\n>> ");
	if "y" in response:
		exit();
	else:
		return;

def createFile(file_path, file_name):
	file = open(file_path + ".txt", "w+");
	file.close();
	print('Text file created with the name "' + file_name + '"');

def append(file_path, file_name):
	text = rawInput("Enter text:\n>> ");
	file = open(file_path + ".txt", "a");
	file.write("\r\n" + text);
	file.close();
	os.system(clear);
	print("Text file appended with " + '"' + text + '"');

def read(file_path, file_name):
	try:
		file = open(file_path + ".txt", "r");
		os.system(clear);
		print("File Name: " + file_name + "\n--------" + file.read());
		file.close();
	except IOError:
		ask = rawInput("File does not exist... Create? (y/n)\n>> ")
		if ask == "n":
			True;
		else:
			createFile(file_path, file_name);

def question():
	os.system(clear);
	print("Choose One " + argcount + ":");
	for arg in optargs:
		print (arg);
	response = raw_input(">> ")
	try:
		response = int(response);
	except ValueError:
		if response == "":
			finished();
			question();
		else:
			rawInput(
				"Error: Options are " + argcount + ". "
				"\nPress enter to continue...");
			question();
	return response;

if __name__ == "__main__":
	main();
