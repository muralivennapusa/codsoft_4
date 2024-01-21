import random
from flask import Flask, request, render_template
import os

app = Flask(__name__)

def computerChoice():
    options=["Rock","Paper","Scissor"]
    choice=random.choice(options)
    return choice

Scoreboard=[0,0]

picFolder=os.path.join('static','pics')
app.config['UPLOAD_FOLDER']=picFolder

@app.route("/")
def index():
    paper=os.path.join(app.config['UPLOAD_FOLDER'],'paper.png')
    rock=os.path.join(app.config['UPLOAD_FOLDER'],'rock.png')
    scissor=os.path.join(app.config['UPLOAD_FOLDER'],'scissor.png')
    return render_template("RPCIndex.html",rock=rock,paper=paper,scissor=scissor)

@app.route("/", methods=["POST"])
def out():
    n = request.form['user_input']
    print(n)
    c=computerChoice()
    if n.lower() not in ["rock","paper","scissor"]:
        winner="Invalid input"
    elif n.lower()==c.lower():
        winner="Draw"
    elif c.lower()=="paper" and n.lower()=="rock":
        winner="Computer Win"
        Scoreboard[0]+=1
    elif c.lower()=="scissor" and n.lower()=="paper":
        winner="Computer Win"
        Scoreboard[0]+=1
    elif c.lower()=="rock" and n.lower()=="scissor":
        winner="Computer Win"
        Scoreboard[0]+=1
    else:
        winner="You Win"
        Scoreboard[1]+=1
    paper=os.path.join(app.config['UPLOAD_FOLDER'],'paper.png')
    rock=os.path.join(app.config['UPLOAD_FOLDER'],'rock.png')
    scissor=os.path.join(app.config['UPLOAD_FOLDER'],'scissor.png')
    
    if c.lower() == 'paper':
        CI=paper
    elif c.lower() == 'rock':
        CI=rock
    elif c.lower() =='scissor':
        CI=scissor

    if n.lower() == 'rock':
        UI=rock
    elif n.lower() == 'paper':
        UI=paper
    elif n.lower() =='scissor':
        UI=scissor
    else:
        UI=CI
    return render_template('RPCPlay.html', Winner = winner,UM=n ,CM=c, CW=Scoreboard[0],UW=Scoreboard[1],rock=rock,paper=paper,scissor=scissor,UI=UI,CI=CI)

if __name__ == "__main__":
    app.run(debug=True)
