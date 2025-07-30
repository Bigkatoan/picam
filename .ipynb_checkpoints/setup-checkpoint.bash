sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip python3-virtualenv python3-picamera2 -y
sudo apt install libcap-dev -y

python3 -m venv myenv --system-site-packages
source venv/bin/activate
pip install --upgrade pip

pip install matplotlib pandas tqdm ipywidgets jupyterlab picamera2

pip install ultralytics

pip install opencv-python==4.5.5.64 "numpy<2"

echo "Code and demo on 'picam' folder"

git clone https://github.com/Bigkatoan/picam.git

echo "source ~/venv/bin/activate" >> .bashrc

echo "Setup complete!"
