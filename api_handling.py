import json

import requests

url = "https://proconvn.duckdns.org"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQsIm5hbWUiOiJQUk9DT05fQk1RIiwiaXNfYWRtaW4iOmZhbHNlLCJpYXQiOjE3MjQ2NDc0NDcsImV4cCI6MTcyNDgyMDI0N30.VvfEIhULZbzagKUni9w-x5gxCwDhYpNDQx4adxeT75I"

headers = {
    "Authorization": token
}


def get_question(question_id):
    question_string = requests.get(f"{url}/question/{question_id}", headers=headers).json()
    question = json.loads(question_string["question_data"])
    return question


def send_answer(question_id, answer):
    payload = {"question_id": question_id, "answer_data": answer}
    res = requests.post(f"{url}/answer", json=payload, headers=headers).json()
    return res["id"]


def get_result(answer_id):
    answer = requests.get(f"{url}/answer/{answer_id}", headers=headers).json()
    score_data = json.loads(answer["score_data"])
    return answer["final_score"]
