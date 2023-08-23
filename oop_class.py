#!?usr/bin/env python
"""
This code is Written by Group 10
Implementation of the OOP class containig mehtods
for the course selector functionality.
Each method was wrritten by a group memeber.
"""
import openai
import json
import requests


class CSelector:
    """_summary_:

    """

    def __init__(self, access_token):
        """_summary_: Constructor iniitialization

        Args:
            access_token (_type_): input access token for openai
        Returns:
            None
        """
        self.access_token = access_token
        self.user_response = ""
        self.courses = ""
        self.url = ""  # store the ibass server url

    def collect_user_input(self, user_input: dict) -> str:
        """_summary_: retrives and processes the user input
           _Author_ :

        Args:
            user_input (dict): _description_

        Returns:
            str: _description_
        """
        stringfyInput = ""

        count = 1

        for key in user_input:
            holder = ""
            holder += f"Question {count}: " + key
            holder += " Answer: " + user_input[key] + " "
            stringfyInput += holder
            count += 1

        self.user_response = stringfyInput
        return stringfyInput

    def validate_user_input(self, user_input: dict) -> bool:
        """_summary_: validates user input
           _Author_ : Hamza Saidu - U18CO1002

        Args:
            user_input (dict): _description_

        Returns:
            bool: Returns True or False
        """
        values = user_input.values()  # extract users answers
        user_input = "".join(values)  # convert answer list to strings
        filterd_user_input = user_input.strip(",.")  # filter user input

        if filterd_user_input.isapha() or filterd_user_input.isalnum():
            return True
        else:
            return False

    def interface_to_algorithm(self, prompt: str, model='gpt-3.5-turbo') -> json:
        """_summary_: Coneects the algorithm to our app
           _Author_ :

        Args:
            model (str, optional): _description_. Defaults to 'gpt-3.5-turbo'.

        Returns:
            json: _description_
        """
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"rote": "system", "content":"Analyze the following question and recommend 5 good courses"},
                {"role": "user", "content": prompt},
                ]
                )
        output = json.dumps(response)  # convert output to json object

        return output

    def pUser_input(self) -> str:
        """_summary_: passees user input into the algo
                      and recives the response
           _Author_ :

        Returns:
            str: retuns result of algorithm (recommended courses)
        """
        response = self.interface_to_algorithm(self.user_response)
        response = json.loads(response)  # convert the json object back
        choice = response.choices[0]
        message = choice.message
        content = message.content
        return content

    def organize_output(self) -> str:
        """_summary_: organize the output from the algorithm
           _Author_:

        Returns:
            str: organized output
        """
        pass

    def query_ibass(self, course: str) -> list[str]:
        """_summary_

        Args:
            course (str): _description_

        Returns:
            list[str]: _description_
        """
        pass

    def filter_courses(self, course: str):
        """_summary_

        Args:
            course (str): _description_
        """
        pass

    def jamb_combo(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        pass

    def DE_combo(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        pass

    def olevel_req(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        pass
