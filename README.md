 🚀 Space Mission Tracker

A Python command-line application for tracking upcoming space launches.

The application uses the **Launch Library 2 API** to retrieve real-time information about upcoming rocket launches and provides convenient tools for searching, filtering, and viewing launch information.


 ✨ Features

* 🚀 View upcoming space launches
* 🛰️ View the next scheduled launch
* 🔎 Search missions by name
* 📊 Filter launches by status
* 📅 Filter launches by date
* 🚀 View rocket information
* 🌍 View launch location
* 📺 Check livestream availability
* 🖼️ View mission image links
* ⚠️ Handle API connection errors


## 🖥️ Application

The application runs directly in the terminal and provides a simple interactive menu:

   text
======================================================================
🚀 SPACE MISSION TRACKER
======================================================================
1. Ближайшие запуски
2. Следующий запуск
3. Поиск миссии
4. Фильтр по статусу
5. Фильтр по дате
6. Выход
======================================================================




## 🛠️ Technologies

* **Python 3**
* **Requests**
* **REST API**
* **JSON**
* **Git & GitHub**
* **Command Line Interface (CLI)**



## 📡 Data Source

Launch information is provided by **The Space Devs — Launch Library 2**.

Official API documentation:

https://thespacedevs.com/llapi



## 📁 Project Structure

   text
space-mission-tracker/
│
├── .gitignore
├── README.md
├── main.py
└── requirements.txt



## ⚙️ Installation

### 1. Clone the repository

   bash
git clone https://github.com/clinchred/space-mission-tracker.git


### 2. Open the project directory

   bash
cd space-mission-tracker


### 3. Create a virtual environment

   bash
python -m venv venv


### 4. Activate the virtual environment

#### Windows

   bash
venv\Scripts\activate


#### Linux / macOS

   bash
source venv/bin/activate


### 5. Install dependencies

   bash
pip install -r requirements.txt



## ▶️ Running the Application

Run:

   bash
python main.py


The program will open the main menu in your terminal.



## 🔎 Available Functions

### 🚀 Upcoming Launches

Displays the five nearest upcoming launches.

### 🛰️ Next Launch

Displays detailed information about the next scheduled launch.

### 🔎 Mission Search

Searches upcoming launches by mission name.

### 📊 Status Filter

Filters launches according to their current status.

### 📅 Date Filter

Shows launches scheduled within a selected number of days.


🎯 Project Goals

This project was created as a practical Python project to develop experience with:

* REST APIs
* JSON data
* HTTP requests
* Date and time processing
* Error handling
* Functions and program structure
* Command-line applications
* Git version control
* GitHub project management



🔮 Future Improvements

Planned features:

* ⭐ Favorite missions
* 🔗 Direct links to launch pages
* 📊 Launch statistics
* 🔎 Advanced search
* 💾 Local data storage
* 🖥️ Graphical user interface
* 🌐 Web version
* 🛰️ More detailed mission information


👨‍💻 Author

Clinchred

Space Mission Tracker is a personal Python project focused on space technology, APIs, and software development.


📄 License

This project is intended for educational and personal use.
