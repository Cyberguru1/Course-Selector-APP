# Course-Selector-APP

This project was an implementation of a course selector app using pyqt5, pyslide and qt-designer.

The aim of this app is to solve the problem of selecting a desired course for Higher School Students, it helps them provide a wide list of courses they could study in Nigerian institution ranging from Universities, Polytechnics, Colleges of Education and so on.

In terms of decision making our app helps the Student in recommending possible course a user can study by asking the user some question ranging on interest, strengths, carrer interests and so on, which the answers to the questions is sent to ChatGpt for processing and the Response feed back to the user to make their final decision.

# Implementation

* The app ask users some series of question to know the opinons of the user this question cover a range of aspects including interests, career aspirations, strengths, preferred learning styles, and more, which can help narrow down the potential name of a course that would suit the user's preferences and goals.
* This questions are now tagged with the answer and sent to Chatgpt for processing to give possible recommendations of courses for the user to select.
* This courses can now be searched in our database where all the courses and institution we have (using Nigeria as case study), this courses have the possible jamb combinations and O'Level requirements a user could use while trying to register for JAMB and selecting desired Institution.
* The app also have a history where all previous searches where stored for reference
* A help menu is also incorporated in order to show the user on how to use the APP

# Technology Used

* **Qt-Designer-Tool**: qt-designer tool was used to create the front end of the gui app, due to time constraints this was an effective way in building the GUI interface to the user where the conceptual model of the user is taking into consideration
* **PyQt5**: This is the python libriray used in collaboration with Qt-Desingner-Tool for creating widgtets, buttons, sliders and so on
* **PySide2**: This a custom libriary used with PyQt5 to add some cool UI to the front-End in order to give it that warm feel and make it Easy, user friendly and enjoyable to use.

# Challenges

Most of the challenges faced while building this project includes:

* Time Constriants
* Debugging Bugs
* Team Work

# Feature Upgrades

Most of the feature upgrade to this app includes:

* User Logging feature
* chat bot feature
* web based version
* offline feature
