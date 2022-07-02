from flask import Flask
import random
import string
import pandas as pd

app = Flask(__name__)



@app.route('/')

def generate_password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    ## length of our password
    length = random.randint(10,20)
    ## shuffling the characters we have in "CHARACTERS"
    random.shuffle(characters)

    ## picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    return("".join(password))

@app.route('/csv')
def calculate_average():
	reader = pd.read_csv('hw.csv')
	avg = reader.mean()
	return {'avg_weight': round(avg[' Weight(Pounds)'], 2),
            '  avg_height': round(avg[' Height(Inches)'], 2)}





if __name__ == '__main__':
    app.run()
