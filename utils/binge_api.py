import json
from typing import List

import requests
from requests import RequestException


class BingeApi:
    url: str = "https://chatgpt-api8.p.rapidapi.com/"
    X_RapidAPI_key: str = "a4b0a931ffmsh51f09a0614f42c1p142c5bjsnb1ddeae5454e"
    X_RapidAPI_host: str = "chatgpt-api8.p.rapidapi.com"
    headers: dict

    def __init__(self) -> None:
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.X_RapidAPI_key,
            "X-RapidAPI-Host": self.X_RapidAPI_host,
        }

    def getAnswerFromApi(
            self, paragraph: str, question: str
    ) -> dict:
        """

        :param paragraph:
        :param question:
        :return:
        """
        payload = self.__create_payload(paragraph=paragraph, question=question)
        response = requests
        try:
            response = requests.post(
                self.url,
                json=payload,
                headers=self.headers,
            )
            return response.json()['text']
        except RequestException:
            print(response.text)



    def __create_payload(self, paragraph: str, question: str) -> List[dict[str, str]]:
        final_question = (
                "From the given paragraph: \n"
                + paragraph
                + "\n"
                + "Answer the following: \n"
                + question
        )

        return [{"content": final_question, "role": "user"}]
