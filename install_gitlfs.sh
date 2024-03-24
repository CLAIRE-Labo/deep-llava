# we also need the git-lfs (need to learn what its exactly used for)
# please don't run this script as it is not yet prepared

#Git-LFS is an extension to Git which is used to manage large files and binary files in a separate LFS store file. By
#doing so it keeps the git repositories at a manageabl size!
#Git-LFS uses pointers (references) to files instead of storing the actual files or binary large objects (blobs) - a type
#of data that stores binaries as one entity - in a Git repository itself.

# ======= IMPORTANT
# first command is installed into the general environment
# second + third commands need to be run in the folder with large files

sudo apt install git-lfs
git lfs install # After installing Git LFS, you need to run the git lfs install command to set up Git LFS for your Git installation
git lfs pull # Finally, you need to run git lfs pull in the folder where you cloned the repository to fetch the large files tracked by Git LFS
