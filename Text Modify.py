import os
optargs = ["1. Create","2. Append","3. Read"];
def main():
	i = 1;
	print("Welcome to my simple text creator and reader!\nThis is version 1.\nI will add more features when my battery is not dying.\nEnjoy!\n\n")
	print("Where shall we manage your files?")
	for i in next(os.walk("."))[1]:
		print ("- "+i);
	folder = raw_input("Enter name of Directory:\n>> ")
	path=("./"+folder+"/");
	while i > 0:
		q = question();
		if type(q) == int:
			fileName = str(raw_input("Please enter file name: \n>> "))
			filePath = path+fileName
			i = job(q, filePath, fileName);
		else:
			print("Please choose number 1-3");
			i = 1;

def job(q, filePath, fileName):
	print(q);
	if q == 1:
		if len(filePath) == 0:
			print("Please enter a file name");
		else:
			create(filePath);
			i = finished();
			return i;
	if q == 2:
		if len(filePath) == 0:
			print("Please enter a file name");
		else:
			append(filePath);
			i = finished();
			return i;
	if q == 3:
		if len(filePath) == 0:
			print("Please enter a file name");
		else:
			read(filePath, fileName);
			i = finished();
			return i;
	else:
		print("Please choose number 1-3");
		return;

def finished():
	w = raw_input("Are you finished? (y/n)\n>> ");
	if w == "y":
		i = 0;
		return i;
	if w == "n":
		i = 1;
		return i;

def crFolder():
	path="/files"
	os.mkdir(path)
	i = finished();
	return i;

def create(filePath):
	f = open(filePath+".txt", "w+");
	f.close();
	print("Text file created with the name "+'"'+fileName+'"');

def append(filePath):
	t = raw_input("Enter text:\n>> ");
	f = open(filePath+".txt", "a");
	f.write("\r\n"+t);
	f.close();
	print("Text file appended with "+'"'+t+'"');

def read(filePath, fileName):
	f = open(filePath+".txt", "r")
	print("File Name: "+fileName+"\n--------"+f.read());
	f.close();

def question():
	print("Choose One (1-3):");
	for i in optargs: print (i);
	q = int(raw_input(">> "));
	return q;

if __name__ == "__main__":
	main();
