from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

players = Blueprint('players', __name__)

#------------------------------------------------------------
# Get all teams from the system
# TESTED - PASSING POSTMAN REQUEST
@players.route('/playerStats_minutes', methods=['GET'])
def get_players():
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT
            P.firstname,
            P.lastname,
            S.*
            FROM players P
            JOIN statistics S ON P.id = S.playerId
            JOIN matches m ON S.matchId = m.id
            WHERE S.totalPlayTime >= '00:30:00'  -- Minimum minutes played in a single game, adjust this as needed
            ORDER BY m.date DESC;

    ''')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
#------------------------------------------------------------