import os

localBaseURL = "."

file_must_exist = [("/preset/login.json", "[]"),
                   ("/preset/seat.json", "[]")]


def detect_integrality():
    for file_info in file_must_exist:
        localURL = localBaseURL + file_info[0]
        if not os.path.exists(localURL):
            with open(localURL, "w") as f:
                f.write(file_info[1])
