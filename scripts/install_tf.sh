#!/bin/zsh

# Step 1: Install MiniForge
echo "Downloading and installing MiniForge..."
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
bash Miniforge3-MacOSX-arm64.sh -b -p $HOME/miniforge3

# Step 2: Initialize Conda for Zsh
echo "Initializing Conda for Zsh..."
$HOME/miniforge3/bin/conda init zsh
source ~/.zshrc

# Step 3: Create a Conda environment
echo "Creating Conda environment 'tf-metal'..."
conda create -n tf-metal python=3.9 -y

# Step 4: Activate the Conda environment
echo "Activating environment 'tf-metal'..."
source activate tf-metal

# Step 5: Install TensorFlow dependencies
echo "Installing TensorFlow dependencies..."
conda install -c apple tensorflow-deps -y

# Step 6: Install pip-tools
echo "Installing pip-tools..."
pip install pip-tools

# Step 7: Compile requirements with pip-tools
echo "Compiling requirements with pip-tools..."
pip-compile requirements.in

# Step 8: Install compiled dependencies
echo "Installing compiled dependencies..."
pip-sync requirements.txt

# Step 9: Verify TensorFlow installation
echo "Verifying TensorFlow installation..."
source activate tf-metal
python -c "import tensorflow as tf; print('TensorFlow version:', tf.__version__)"

# Step 10: Verify PyTorch and Transformers installation
echo "Verifying PyTorch and Transformers installation..."
python -c "import torch; print('PyTorch version:', torch.__version__)"
python -c "import transformers; print('Transformers version:', transformers.__version__)"

echo "Installation completed successfully!"
