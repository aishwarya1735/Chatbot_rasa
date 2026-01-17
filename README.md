Voice-Controlled PC Assistant

It is a Machine Learning–based voice assistant that enables full PC control through voice commands. After secure user authentication, Leo automates system operations, applications, and daily information tasks, providing a hands-free and intelligent desktop experience.

- Key Capabilities :

Control system functions: volume, brightness, battery status, screenshots, camera, alarms, shutdown, and restart

Media & app automation: YouTube (play & download), WhatsApp, Chrome, music playback

Utilities & information: date, time, temperature, news updates, location, jokes, and facts

Productivity features: notes, reminders, and schedule notifications

File access: open system drives (C, D, E, F)

- Security & Authentication

Face recognition–based user verification

Password authentication as a fallback if face recognition fails

Commands are enabled only after successful authentication

- Face Recognition Setup

Run sample_generator.py to collect face samples (stored in the samples/ folder)

Run Model_Trainer.py to train the model and generate files in the trainer/ folder

- How to Run

Install dependencies using requirements.txt

Start the assistant by running script.py

Activate using the voice command “Hey Rasa”

Authenticate and issue commands

Deactivate using “Sleep”, “You need a break”, or “Quit”

Reactivate anytime with “Hey Rasa”

- Additional Information

Command handling logic is implemented in the exe() function

Security workflow is defined in the security() function inside Rasa.py
