from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/api', methods=['Get'])
def get_info():
    slack_name = request.args.get('israel precious')
    track = request.args.get( 'backend' )

  # Current day of the week and UTC time
    current_day = datetime.datetime.utcnow().strftime('%A')
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")


 # Github URL of the file being run and the full source code
    github_file_url = "nil"
    github_repo_url = "nil"


# Status code of success
    status_code = 200

    response = {
            "slack_name": slack_name,
            "current_day": current_day,
            "current_utc_time": current_utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": status_code

            }

    return jsonify(response)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
