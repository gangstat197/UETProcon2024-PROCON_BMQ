import requests

url = "https://proconvn.duckdns.org"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQsIm5"
                     "hbWUiOiJQUk9DT05fQk1RIiwiaXNfYWRtaW4iOmZhbHNlLCJpYXQi"
                     "OjE3MjQ2NDc0NDcsImV4cCI6MTcyNDgyMDI0N30.VvfEIhULZbzag"
                     "KUni9w-x5gxCwDhYpNDQx4adxeT75I"
}


def get_question(question_id):
    question = requests.get(f"{url}/question/{question_id}", headers=headers).json()
    return question


def send_answer(question_id, answer):
    payload = {"question_id": question_id, "answer_data": answer}
    res = requests.post(f"{url}/answer", json=payload, headers=headers).json()
    return res["id"]


def get_result(answer_id):
    answer = requests.get(f"{url}/answer/{answer_id}", headers=headers).json()
    return answer["score_data"]

