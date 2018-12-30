import os
optargs = ["1. Create","2. Append","3. Read","4. Change Directory"];
argcount = "1-"+str(len(optargs));
path = "./";
last = (os.path.split(os.path.abspath("./"))[0]+"/");

def main():
	on = 1; #used for while loop
	print(
		"Welcome to my simple text creator and reader!\n"
		"This is version 1.\n"
		"I will add more features when my battery is not dying.\n"
		"Enjoy!");
	#following is used to list and determine directory folder and set path
	global path;
	global last;
	print(pickDirectory(path, last));
	#main while loop follows
	while on > 0:
		#ask which option to use
		response = question();
		if type(response) == int:
			job(response);
		else:
			#if a number is not entered, starts loop over
			print("Error: Please choose number " + argcount + ":");
			on = 1;

def pickDirectory(path_local, last_local):
	global path;
	global last;
	print("\nWhere shall we manage your files?");
	print("Current Path: " + path_local);
	print("Last Path: " + last_local);
	for folder in next(os.walk(path_local))[1]:
		print ("- " + folder);
	print("- ..");
	folder = raw_input("Enter name of Directory (Use '..' to go back):\n>> ");
	if len(folder) == 0:
		answer = raw_input(
			"This is your path: " + path_local + ".\n"
			"Any changes? (n/y)\n>>");
		if answer == "y":
			pickDirectory(path_local, last_local);
		else:
			path = path_local;
			last = last_local;
	elif folder == "..":
		if path_local == "//":
			pickDirectory(path, last);
		else:
			if last == "./":
				path = "./";
				last = (os.path.split(os.path.abspath("./"))[0]+"/");
			else:
				path = last;
				last = (os.path.split(os.path.split(path)[0]))[0]+"/";
			pickDirectory(path, last);
	else:
		path_new = (path_local + folder + "/");
		if not os.path.exists(path_new):
			answer = raw_input("Folder does not exist. Create? (y/n)\n>>")
			if answer == "n":
				path = path_local;
				last = last_local;
				pickDirectory(path, last);
			else:
				os.makedirs(path_new);
		answer = raw_input(
			"This is your path: " + path_new + ".\n"
			"Any changes? (n/y)\n>>");
		if answer == "y":
			if path_new == (os.path.abspath("./")+"/"):
				path = "./";
				last = (os.path.split(os.path.abspath("./"))[0]+"/");
			else:
				path = path_new;
				last = path_local;
			pickDirectory(path, last);
		else:
			path = path_new;
			last = path_local;

def job(response):
	if response == 1:
		filePath, fileName = fileNaming();
		create(filePath, fileName);
		finished();
	if response == 2:
		filePath, fileName = fileNaming();
		append(filePath, fileName);
		finished();
	if response == 3:
		filePath, fileName = fileNaming();
		read(filePath, fileName);
		finished();
	if response == 4:
		global path
		global last
		pickDirectory(path, last);
	else:
		print("Error: Please choose number " + argcount + ":");

def fileNaming():
	print ("Available files:");
	for files in next(os.walk(path))[2]:
		print("- "+str(os.path.splitext(files)[0]));
	print("");
	fileName = str(raw_input("Please enter file name: \n>> "))
	filePath = path + fileName
	while len(filePath) == 0:
		print("Please enter a file name");
		fileNaming();
	return filePath, fileName

def finished():
 	response= raw_input("Are you finished? (y/n)\n>> ");
	if response == "n":
		return;
	if response == "y":
		exit();
	else:
		print("Answer with y or n.");
		finished();

def crFolder():
	path = "/files"
	os.mkdir(path)
	on = finished();
	return on;

def create(filePath, fileName):
	file = open(filePath + ".txt", "w+");
	file.close();
	print('Text file created with the name "' + fileName + '"');

def append(filePath, fileName):
	text = raw_input("Enter text:\n>> ");
	file = open(filePath + ".txt", "a");
	file.write("\r\n" + text);
	file.close();
	print("Text file appended with " + '"' + text + '"');

def read(filePath, fileName):
	try:
		file = open(filePath + ".txt", "r");
		print("File Name: " + fileName + "\n--------" + file.read());
		file.close();
	except IOError:
		ask = raw_input("File does not exist... Create? (y/n)\n>> ")
		if ask == "n":
			True;
		else:
			create(filePath, fileName);

def question():
	print("Choose One " + argcount + ":");
	for arg in optargs:
		print (arg);
	response = raw_input(">> ")
	try:
		response = int(response);
	except ValueError:
		if response == "":
			finished()
		else:
			question();
	return response;

if __name__ == "__main__":
	main();
