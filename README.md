# Benchmark Setup

### First create and run a virtual environment in the working directory:

`pip install virtualenv`

`python3 -m venv <venv_name_here>`

`source <venv_name_here>/bin/activate`

### Then install dependencies:
`pip3 install psutil`
`pip3 install PyQt6`
`pip3 install PySide2`

### Ensure that you can execute the script:
`chmod +x ./runscript`

### Then run the script and wait for data to aggregate:
`./runscript`

## About runscript:

Can uncomment and adjust for loop to run however many times you want. If on local machine that has xdg installed, can also uncomment that line to have the
image opened once the script is complete. If on a non-local machine, leave commented and retreive the generated image to local system before opening.
