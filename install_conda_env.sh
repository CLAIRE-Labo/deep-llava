# Download and install Miniforge (an equivalent of Miniconda)
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh" -O ~/miniforge.sh
bash ~/miniforge.sh -b -p ~/miniforge3

# Delete installer
rm ~/miniforge.sh

# Activate base env and run init for the future
source ~/miniforge3/etc/profile.d/conda.sh

# create the llava virtualenv
conda create -n llava python=3.10 -y
conda activate llava


