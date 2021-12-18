import os
import shutil

# YOU SHOULD ALWAYS LET THIS PROGRAM RUN TO COMPLETION

# a python program contains a directory where the work happens
print(os.getcwd())
print(os.listdir())
print(os.path.exists("image_load_save.py")) #checks current directory if this file exists

os.chdir("test_file_tree") #you can always change your directory

os.mkdir("generated_folder") #throws error if already exists
os.chmod("generated_folder", 0o777) #you can change permissions
shutil.copyfile("a.txt", "work_dir/a_copy.txt") #does not copy metadata
shutil.copy("b.txt", "work_dir/b_copy.txt") #copies everything
shutil.copytree("work_dir", "generated_folder_1") #this can't be an existing directory
shutil.move("a.txt", "work_dir/a.txt")


input("press enter to revert all changes")
os.remove("work_dir/b_copy.txt") #this is how you remove a file
os.remove("work_dir/a_copy.txt") #this is how you remove a file
shutil.move("work_dir/a.txt", "a.txt") #moves back the file we just moved
# os.rmdir("generated_folder") #only works in blank directories
shutil.rmtree("generated_folder") #deletes this folder
shutil.rmtree("generated_folder_1") #deletes this folder