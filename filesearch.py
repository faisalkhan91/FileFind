#!/usr/local/bin/python3

import sys
import os

SearchDir = "/"
SearchExt = ".mp3"  # Default extension.

numargs = len(sys.argv)

if numargs > 3:
	print("Error - too many arguments supplied.")
	sys.exit()
elif numargs == 2:
	if sys.argv[1][0] == ".":
		SearchExt = sys.argv[1]
	else:
		if os.path.isdir(sys.argv[1]):
			SearchDir = sys.argv[1]
		else:
			print("Error - name is not a valid directory")
			sys.exit()
elif numargs == 3:
	if sys.argv[1][0] == ".":
		SearchExt = sys.argv[1]
		if os.path.isdir(sys.argv[2]):
			SearchDir = sys.argv[2]
		else :
			print("Error - name is not a valid directory")
			sys.exit()
	else :	
		if os.path.isdir(sys.argv[1]):
			SearchDir = sys.argv[1]
		else :
			print("Error - name is not a valid directory")
			sys.exit()
		if sys.argv[2][0] == ".":
			SearchExt = sys.argv[2]
		else :
			print("Error - search extension does not contain a period.")
			sys.exit()


def findfile (searchdir, searchext):

	print("Searchdir = ", searchdir, "Searchext = ", searchext)
	foundfiles = []
	contents = os.listdir(searchdir)
	# print(contents)

	for name in contents :
		if os.path.isfile(os.path.join(searchdir, name)):
			# print("found a file", name)
			if name.endswith(searchext):
				foundfiles.append(os.path.join(searchdir, name))
		elif os.path.isdir(os.path.join(searchdir, name)):
			# print("found a directory", name)
			tempfiles = findfile(os.path.join(searchdir, name), searchext)
			foundfiles.extend(tempfiles)

	return foundfiles


def findfile2(searchdir, searchext):

	os.chdir(searchdir)
	print("Searchdir = ", os.getcwd(), "Searchext = ", searchext)
	foundfiles = []
	contents = os.listdir(".")
	# print(contents)

	for name in contents:
		if os.path.isfile(name):
			# print("found a file", name)
			if name.endswith(searchext):
				foundfiles.append(os.path.join(os.getcwd(), name))
		elif os.path.isdir(name):
			# print("found a directory", name)
			tempfiles = findfile2(name, searchext)			
			foundfiles.extend(tempfiles)

	os.chdir("..")
	return foundfiles


# allfiles = findfile(SearchDir, SearchExt)
allfiles = findfile2(SearchDir, SearchExt)

for name in allfiles:
	print(name)

