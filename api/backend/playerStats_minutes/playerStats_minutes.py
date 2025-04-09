from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

playerStatsByMinutes = Blueprint('playersStats_minutes', __name__)

#------------------------------------------------------------
@playerStatsByMinutes.route('/playerStats_minutes', methods=['GET'])
def get_playersStats_minutes():
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT
            P.firstname,
            P.lastname,
            S.*
            FROM players P
            JOIN statistics S ON P.id = S.playerId
            JOIN matches m ON S.matchId = m.id
            WHERE S.totalPlayTime >= %s  -- Minimum playtime placeholder
            ORDER BY m.date DESC;
    ''')  
    
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
#------------------------------------------------------------