First create and run a virtual environment in the working directory

pip install virtualenv
python3 -m venv <venv_name_here>
source <venv_name_here>/bin/activate

Then install dependencies:
pip3 install psutil

Ensure that you can execute the script
Chmod +x ./runscript

Then run the script and wait for data to aggregate:
./runscript
