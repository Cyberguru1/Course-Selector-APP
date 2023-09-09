########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################
# Custom import
import speedtest
from PySide2.QtSql import QSqlDatabase, QSqlQueryModel
import openai
import sqlite3
########################################################################

# IMPORT Custom widgets
from Custom_Widgets.Widgets import *

# INITIALIZE APP SETTINGS
settings = QSettings()

########################################################################

# setting openapi access token key
openai.api_key = "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" # openai chatgpt access token 

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.inc_value = 0
        self.inc = 0
        self.currQ = 1
        self.questions_list = [
            "Click Next To Start!!!",
            "What are your primary areas of interest for studying at the university?",
            "Which subjects or fields do you find most fascinating?",
            "Are you interested in pursuing a career in the sciences, arts, business, or something else?",
            "Do you have a specific passion or hobby that you would like to incorporate into your future studies?",
            "What kind of activities or topics do you enjoy reading or learning about in your free time?",
            "How do you envision yourself contributing to society through your chosen field of study?",
            "Do you prefer working with hands-on practical tasks or theoretical concepts and analysis?",
            "What are your career aspirations or professional goals after completing your university education?",
            "Are there any specific industries or sectors you are interested in working in after graduation?",
            "What personal strengths and skills do you believe will be valuable in your chosen field of study?",
            "How do you handle challenges and setbacks in your academic or personal life?",
            "Do you prefer a comprehensive and broad-based course or a more specialized and focused one?",
            "Would you like to explore interdisciplinary courses that combine multiple subjects?",
            "How important is it for you to have engaging and interactive lectures and classes?",
            "Would you like your course to include practical projects or real-world applications?"
        ]

        self.quesAnswer = {}


        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        # loadJsonStyle(self, self.ui, jsonFiles = {
        #     "mystyle.json", "style.json"
        #     }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

        self.ui.queLabel.setText(QCoreApplication.translate("MainWindow", u""+self.questions_list[0], None))
        self.ui.ansInput.setHidden(True)

        ## Select page settings

                ## setting up the progress barr ** this field was updated **
        self.ui.selectProg.updateFormProgressIndicator(
                # Set font color
                color = "#fff", 
                # Set fill color
                # fillColor = "blue", 
                # Set fill color for warnings
                warningFillColor = "orange ",
                theme = 4,
                # Set fill color for errors
                errorFillColor = "red",
                # Set fill color for success
                successFillColor = "blue",
                # Set number of progress steps(default is 5)
                formProgressCount = 15,
                # Set progress animation duration
                formProgressAnimationDuration = 1000, #1seconds
                # Set progress animation easing curve
                formProgressAnimationEasingCurve = "OutInBounce",
                # Set progress container height
                height = 80,
                # Set progress container width
                width = 1000,
                # Set default progress percentage
                startPercentage =  0 #start
        )

        # set submit button to hidden
        self.ui.submitBtn.setHidden(True)
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)                                                                  
        

        # action buttons for select course page
        self.ui.nextBtn.clicked.connect(lambda: self.incProgress())
        self.ui.prevBtn.clicked.connect(lambda: self.decProgress())
        self.ui.endBtn.clicked.connect(lambda: self.incProgress(End=True))
        self.ui.startBtn.clicked.connect(lambda: self.decProgress(End=True))
        self.ui.select_courseBtn.clicked.connect(lambda: self.resetQuestion())
        self.ui.testBtn.clicked.connect(lambda: self.testConnection())
        self.ui.submitBtn.clicked.connect(lambda: self.submitQues())
        self.ui.tableView.clicked.connect(self.row_clicked)
        self.ui.instSearch.textChanged.connect(self.update_filter)

        # ININTIALIZING DATABASE
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("ibass_database.db")
        self.conn = sqlite3.connect('ibass_database.db')
        self.cursor = self.conn.cursor()
        
        if not self.db.open():
            print("Database connection failed.")
            sys.exit(1)

        self.model = QSqlQueryModel(self)
        self.model.setQuery("SELECT UniName,title,SubInstType FROM Entities ORDER BY UniName")        
        self.ui.tableView.setModel(self.model)


  
    def incProgress(self, End=False):
        """_summary_: increments the forms progress

        Args:
            End (bool, optional): _description_. Defaults to False.
        """

        self.inc_value += 70

        if self.inc_value == 1050:
            self.inc_value = 980

        if End:
            self.inc_value = 980
            self.currQ = len(self.questions_list) - 1
        
        self.nextQuestion()
        self.ui.selectProg.updateFormProgress(self.inc_value)

 
    def decProgress(self, End=False):
        """_summary_: decrements the forms progress

        Args:
            End (bool, optional): _description_. Defaults to False.
        """
        
        self.inc_value -= 70

        if self.inc_value < 0:
            self.inc_value = 0

        if End:
            self.inc_value = 0
            self.currQ = 2
        
        self.prevQuestion()
        self.ui.selectProg.updateFormProgress(self.inc_value)


    def nextQuestion(self):
        """
        _summary_:
                Generates the next question and save the response of
                the preveious question into the dictionary
        """

        # Open enter space        
        self.ui.ansInput.setHidden(False)
        if self.currQ > 0 and self.currQ < len(self.questions_list):
            question = self.questions_list[self.currQ]
            self.ui.queLabel.setText(QCoreApplication.translate("MainWindow", u""+question, None))
        
        if self.currQ > 1 and self.currQ - 1 < len(self.questions_list):
            question = self.questions_list[self.currQ - 1]
            response = self.ui.ansInput.text()
            
            # insert the response if it's for the first time
            if question not in list(self.quesAnswer.keys()):
                self.quesAnswer[question] = response

            # update the answers if it exists
            if response != "" and response != self.quesAnswer[question]:
                self.quesAnswer[question] = response


        # perform an action when the last question is reached
        if self.currQ == 16:
            self.changeState(event=True)


        # increment while setting bounds for the next question
        self.currQ += 1
        if self.currQ > len(self.questions_list):
            self.currQ = len(self.questions_list)

        # clear the response
        self.ui.ansInput.clear()
        


    def prevQuestion(self):

        # change state back:
        self.changeState(event=False)

        # decrement the next question
        self.currQ -= 1

        # set bounds for the first question
        if self.currQ <= 2:
            self.currQ = 2

        # clear previous answers shown
        self.ui.ansInput.clear()

        # display the question
        question = self.questions_list[self.currQ - 1]
        self.ui.queLabel.setText(QCoreApplication.translate("MainWindow", u""+question, None))

        # display previous answers
        if question in list(self.quesAnswer.keys()):
            answer = self.quesAnswer[question]
            self.ui.ansInput.setText(answer)
        

    def resetQuestion(self):
        """_summary_:
                      Reset the answered question back to its original state
            Returns: None
        """

        self.inc_value = 0
        self.inc = 0
        self.currQ = 1
        self.quesAnswer = {}
        self.ui.queLabel.setText(QCoreApplication.translate("MainWindow", u""+self.questions_list[0], None))
        self.ui.ansInput.setHidden(True)
        self.ui.nextBtn.setHidden(False)
        self.ui.submitBtn.setHidden(True)

        # reset progress to beginning state
        self.ui.selectProg.updateFormProgress(0)


    def changeState(self, event=None):
        """_summary: Change the next button to submit button base on bool event
        """
        # if true hide next button and display submit button
        if event:
            self.ui.nextBtn.setHidden(True)
            self.ui.submitBtn.setHidden(False)

        # else perform the reverse case
        else:
            self.ui.nextBtn.setHidden(False)
            self.ui.submitBtn.setHidden(True)

    def bytes_to_mb(self, Cbytes):
        """_summary_

        Args:
            Cbytes (_type_): bytes read

        Returns:
            _type_: integer
        """
        KB = 1024
        MB = KB * 1024

        return int(Cbytes/MB)
    

    def testConnection(self):
        """_summary_ test connection
        """
        test = speedtest.Speedtest()
        down_speed1 = self.bytes_to_mb(test.download())
        down_speed = f"{down_speed1} Mbps"

        up_speed = self.bytes_to_mb(test.upload())
        up_speed = f"{up_speed} Mbps"

        self.ui.upLabel.setText(up_speed)
        self.ui.downLabel.setText(down_speed)

        if down_speed1 >= 10:
            self.ui.connRes.setText("Connection is Good!!!")
        else:
            self.ui.connRes.setText("Connection is Moderate!!!")

    def row_clicked(self, index: QModelIndex):
        # Get the row number of the clicked cell
        row = index.row()

        # Retrieve all data for the clicked row
        row_data = []
        for col in range(self.model.columnCount()):
            data = self.model.index(row, col).data()
            row_data.append(data)

        # Print the whole row's content
        self.displayReq(row_data)


    def displayReq(self, row_data):
        """Callback"""
        uniname_value = row_data[0]
        title_value = row_data[1]

        # Execute the SQL query to fetch the data
        query = """
               SELECT de_requirements, utme_requirements, subjects
               FROM Entities
               WHERE Uniname = ? AND title = ?
            """
        self.cursor.execute(query, (uniname_value, title_value))

        # Fetch the result (assuming there's only one matching row)
        result = self.cursor.fetchone()
        
        # Display contents in right menu
        title = title_value + ", " + uniname_value
        self.ui.uniName.setText(title)
        self.ui.deEntry.setHtml(result[0])
        self.ui.utmeEntry.setHtml(result[1])
        self.ui.jambEntry.setHtml(result[2])

    def update_filter(self):
        # Retrieve the search text from the QLineEdit
        search_text = self.ui.instSearch.text()

        # Construct the query with a filter
        query = f"""
            SELECT UniName, title, SubInstType
            FROM Entities
            WHERE UniName LIKE '%{search_text}%' OR title LIKE '%{search_text}%'
        """

        # Set the query in the QSqlQueryModel to update the filter
        self.model.setQuery(query)

        
    def interface_to_chatgpt(self, prompt: str, model='gpt-3.5-turbo') -> json:
        """_summary_: Coneects the algorithm to our app
           _Author_ :

        Args:
            model (str, optional): _description_. Defaults to 'gpt-3.5-turbo'.

        Returns:
            json: _description_
        """
         # link the access token here
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content":"Analyze the following dictionary item where the \
                 key is question and value is answer then recommend 5 good courses, output should be in html format"},
                {"role": "user", "content": f"{prompt}"},
                ]
                )
        choice = response.choices[0] # convert output to json object
        message = choice.message
        content = message.content
        self.ui.resultEntry.setHtml(content)


    def submitQues(self):
        """_summary_
        """
        self.interface_to_chatgpt(self.quesAnswer)
        self.resetQuestion()
    
    





########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
