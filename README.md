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

## **APP UI**

- **Home Page**

![](https://media.discordapp.net/attachments/975033575416143962/1148199269535334450/home_page_g1.png?ex=653f81e6&is=652d0ce6&hm=d0a96b164edfca5c6e28d5cba9c19f2315c8ef6bf53dde5d4a503c5f0baa65dc&=&width=984&height=627)


- **Select Course Page**

![](https://media.discordapp.net/attachments/975033575416143962/1148193364076929124/select1_g1.png?ex=653f7c66&is=652d0766&hm=939478cda8edb79aaf5f8925489cf313485476fe4588758752da337b73a369da&=&width=981&height=627)

![](https://media.discordapp.net/attachments/975033575416143962/1148193363678474321/select2_g1.png?ex=653f7c66&is=652d0766&hm=34f0a48ad3d7dad6ee60b36b04a849d6e60422c04e1397bde13e715c6c97d066&=&width=989&height=627)


- **Internet Connection Test Page**
- ![](https://media.discordapp.net/attachments/975033575416143962/1148193364408283137/connection_g1.png?ex=653f7c66&is=652d0766&hm=2906834ac961e185e5436920ec2da13a63b8cceec474a0f9885c16d507af80cd&=&width=980&height=627)
- **Notification Page**
- ![](https://media.discordapp.net/attachments/975033575416143962/1148193364697677905/notifcation_g1.png?ex=653f7c66&is=652d0766&hm=cd56e9f2f498cbebf2fa77a62820867a3b0c39096082a65c5a8b8b3b6695516e&=&width=986&height=627)


# Technology Used

* **Qt-Designer-Tool**: qt-designer tool was used to create the front end of the gui app, due to time constraints this was an effective way in building the GUI interface to the user where the conceptual model of the user is taking into consideration
* **PyQt5**: This is the python libriray used in collaboration with Qt-Desingner-Tool for creating widgtets, buttons, sliders and so on
* **PySide2**: This a custom libriary used with PyQt5 to add some cool UI to the front-End in order to give it that warm feel and make it Easy, user friendly and enjoyable to use.

# Challenges

Most of the challenges faced while building this project includes:

* Time Constriants
* Debugging Bugs

# Feature Upgrades

Most of the feature upgrade to this app includes:

* User Logging feature
* chat bot feature
* web based version
* offline feature
