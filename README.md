
# Attendance marking system using multiple face recognition system
This is a graphical interface for a face recognition-based attendance system using Tkinter and AI technologies.



## Description
The project utilizes Tkinter for GUI, PIL for image handling, and various modules for different functionalities such as student registration, training data, face detection, attendance reporting, and more.

## Usage
This program offers several functionalities accessible via the graphical interface:

Student Information: Collects and manages student details.
Train Data: Trains the system with student data for recognition.
Face Detector: Detects faces using AI.
Student Attendance: Generates attendance reports.
Student Photos: Accesses stored student images.
Developers: Provides information about the developers.
Help: Offers assistance and guidance.
Exit Application: Closes the application.

## Directory Structure
- attendance_report/
- data/
- database/
- public/
- .gitignore
- about.py
- attendance.py
- classifier.xml
- config.ini
- db_connection.py
- Desktop_Icon.ico
- face_recognition.py
- haarcascade_frontalface_default.xml
- help.py
- main.py
- requirements.txt
- setup.py
- student.py
- tcl86t.dll
- tk86t.dll
- train.py



## Installation
Install my-project with npm

```bash
  git clone (https://github.com/ashwiniojha143/AI-Attendance-Management-System)
  cd Desktop_application
  pip install -r requirements.txt

```

## Reuired Folder 
make manually folder 
- data
- attendance_report
- config.ini should have 
  
  ```bash
  [Database]
  DB_HOST = localhost
  DB_USER = root
  DB_PASSWORD = root
  DB_NAME = facerecognizer

  [RapidAPI]
  API_KEY = add your api key of rapid ai
  HOST = chatgpt-gpt4-ai-chatbot.p.rapidapi.com

  ```
    
    
## Contributing
Contributions to this project are welcomed and appreciated! You can contribute by:

Reporting Bugs: If you encounter any bugs or issues, please create a detailed GitHub issue describing the problem.

Feature Requests: Suggest new features or improvements that could enhance the project's functionality.

Code Contributions: Fork the repository, create a new branch, and submit a pull request with your changes. Ensure your code follows the project's coding style and conventions.

Documentation: Enhance README files, add code comments, or improve documentation to make the project more understandable and accessible.

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.Clone the forked repository to your local machine:
```bash
git clone https://github.com/YourUsername/Desktop_application.git

git checkout -b feature/YourFeature

git commit -m "Add your commit message here"

git push origin feature/YourFeature


```


## Authors
- [@octokatherine](https://www.github.com/octokatherine)

1. Prof. Dr. Ajay Kushwaha
Role: Project Guide

Description: Prof. Dr. Ajay kushwaha has provided guidance and mentorship for this project, offering expertise and insights into the field of [AI, Computer Vision].

2. Ashwini Ojha
Role: Developer

Description: Ashwini Kr. OJha, an Electronics and Telecommunication student at [BVUCOEP], has contributed to various aspects of the project, including [Deep Learning, Full Stack]. I am using Git in this project as learning way.

2. Ankit Raj
Role: Developer

Description: Ankit Raj, also an Electronics and Telecommunication student at [BVUCOEP], has been actively involved in [Full stack , Developer].

3. Ankit Raj
Role: Developer

Description: Ankit Raj, an Electronics and Telecommunication student at [BVUCOEP], has contributed significantly to [IOT , Developer].

4. Somya Kumari
Role: Developer

Description: Somya Kumari, an Electronics and Telecommunication student at [BVUCOEP], has contributed significantly to [Database Handling].


