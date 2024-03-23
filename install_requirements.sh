# create the llava virtualenv
conda create -n llava python=3.10 -y
conda activate llava
pip install --upgrade pip  # enable PEP 660 support
pip install -e .

# install the training packages
pip install -e ".[train]"
pip install flash-attn --no-build-isolation
