# crude but working example of how to use wolfram engine to answer search query from terminal

import wolframalpha

question = input("Question: ")
app_id = "PJQ2QT-R7TTT6TPY5"
client = wolframalpha.Client(app_id)

res = client.query(question)
answer = next(res.results).text

print(answer)