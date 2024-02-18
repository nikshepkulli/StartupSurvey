# comments
from flask import Flask, render_template, request

app = Flask(__name__)


class TeamMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Startup:
    def __init__(self, ceo, cto, cfo, board_members):
        self.ceo = ceo
        self.cto = cto
        self.cfo = cfo
        self.board_members = board_members


startup_team = Startup(
    ceo=TeamMember("John Doe", "CEO"),
    cto=TeamMember("Jane Smith", "CTO"),
    cfo=TeamMember("Alice Johnson", "CFO"),
    board_members=[
        TeamMember("Bob Brown", "Board Member"),
        TeamMember("Emma Wilson", "Board Member")
    ]
)


@app.route('/')
def index():
    return render_template('index.html', team=startup_team)


@app.route('/survey', methods=['POST'])
def survey():
    problem = request.form['problem']
    # Here you would process the survey response (store it, analyze it, etc.)
    return 'Survey response received: ' + problem


if __name__ == '__main__':
    app.run(debug=True)
