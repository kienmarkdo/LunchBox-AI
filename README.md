# Overview

Real-time people detection with Slack integration to notify Trend Ottawa employees how long the line is to get food on Wednesdays.

Utilizes computer vision, image processing, and existing deep learning models to detect people in a live camera feed.

*Developed by Hadi Srour, Hajar Assim, Kien Do, and Jeyason Jeyaparan.*

# Demo
[![LunchBox AI Demo Video](https://i9.ytimg.com/vi/ehM2xgS4xX8/mqdefault.jpg?sqp=CPT-r70G-oaymwEmCMACELQB8quKqQMa8AEB-AHUBoAC4AOKAgwIABABGGUgZShlMA8=&rs=AOn4CLBWp_w8GXqx8kdQvIJ3FEuuW0Kb-w)](https://youtu.be/ehM2xgS4xX8)
> Won 1st place at Trend Micro Canada 2024's company-wide 24-hour hackathon. LunchBox AI is a lightweight computer vision solution designed to track the number of people waiting in line for food and send real-time notifications to employees via Slack. Developed in collaboration with fellow CO-OP students from the University of Ottawa and Carleton University.

## Setup
- Open the terminal in the root of the project
- Create a virtual environment
```console
python3 -m venv venv          # create the venv
source venv/bin/activate      # activate the venv
```
- Install project dependencies
```console
pip3 install opencv-python
pip3 install tensorflow
pip3 install slack_bolt
pip3 install slack_sdk
pip3 install slackclient
```
- Open a new terminal and run the people detection program
```console
python3 main.py
```
> [!NOTE]  
> Click "Allow" when your code editor asks for permission to open the camera.

- Open another terminal to start up the Slack server to send/receive messages
```console
python3 slack.py
```
- Use the bot by going to your channel's Integrations tab --> App --> Add "LunchBox AI"
- Begin using it with the following commands
```console
@LunchBoxAI
@LunchBoxAI /setmenu Chicken and rice
@LunchBoxAI /setmenu leftovers
@LunchBoxAI /setmenu end
```
