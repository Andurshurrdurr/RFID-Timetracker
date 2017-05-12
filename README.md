# RFID Timetracker

This is an application to use RFID and the toggl api to do some automation with timetracking. I coded this a brist friday morning.

I had a cheap M302 RFID scanner lying around, so I thought I would use it to do some time tracking automation. The program communicates to the scanner through serial and uses the toggl API to initiate timetracking.

This version is unusable right now, I just want to put it under Version Control so I can easily move it between my machines.

## Requirements
You need python 2.7 and pip to install the requirements

## Getting started
0. Optional: Set up a virtualenv with `$ python virtualenv ./venv/` and `$ source venv/bin/activate` - This step makes life easier
1. Install requirements with pip `$ pip install -r requirements.txt`
2. Connect the RFID card reader to USB
3. Fill in the access token and desired project in app.py (will become a config file)
4. Run the application: `$ python app.py`

## Demo

// I will add this very soon

## License

Code is published under the MIT License. See the license file

## Thanks to

Thanks to @matthewdowney for his python wrapper for the toggl api. Check out his work at
https://github.com/matthewdowney/TogglPy

And thanks to @abbbi for his M302 rfid scanner library. A slightly modified version is in the ScanRFID.py file (I just made it a function)
https://github.com/abbbi/mifare
