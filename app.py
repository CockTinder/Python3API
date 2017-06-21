#!.venv/bin/python3

from flask import Flask, jsonify, redirect, request

import oauth2client
import googleAuth

app = Flask(__name__)

#create 404 msg
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": {"type": 404, "message": "Not Found"}, "msg": "pleas look at api specs on https://github.com/CockTinder/Python3API"}), 404

@app.route('/')
def index():
    return jsonify({"error": {"type": 410, "message": "Gone"}, "msg": "pleas look at api specs on https://github.com/CockTinder/Python3API"}), 410

@app.route("/auth/google")
def getGoogleURl():
    return redirect(googleAuth.googleCallbackUrl())

@app.route("/auth/google/callback")
def oath2Callback():
    if 'code' not in request.args:
        print("not auth")
        return redirect("/"), 403
    else:
        auth_code = request.args.get('code')
        try:
            creds = googleAuth.auth(auth_code)
            print(creds)
            print(creds.to_json())
            return jsonify(creds.to_json())
        except oauth2client.client.FlowExchangeError as e:
            print(e)
    return "test"

@app.route("/test")
def test():
    return jsonify({"access_token": "ya29.GltwBKUTfYCr2VtT4G1s7XuvSy2hiZ7rnw9zzOPqFN6avUjgkzBIGez64jZE4LCJD4KBwIDyMpyKYVhEF_YyYnokJkT6MTwrJiuzSdTISDrLA4O0T8SZ7WqMcAVT", "user_agent": None, "client_secret": "pbnk6rdOUt4NShQJFeXkLoL5", "_class": "OAuth2Credentials", "id_token": {"email": "filabe.fb@gmail.com", "aud": "1018179507123-ugm6t8mb7alnbldmfiibeuo0kjr2dvbj.apps.googleusercontent.com", "exp": 1498070897, "sub": "117012649305154251195", "azp": "1018179507123-ugm6t8mb7alnbldmfiibeuo0kjr2dvbj.apps.googleusercontent.com", "email_verified": True, "iss": "accounts.google.com", "iat": 1498067297, "at_hash": "FlYyo6Nxoqs4LY4YJsFJhQ"}, "id_token_jwt": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImVjZmZlZmYyZjYzZjhlOThlZjM2YWRiZGViNzI5MTVlM2E0NmVmMmUifQ.eyJhenAiOiIxMDE4MTc5NTA3MTIzLXVnbTZ0OG1iN2FsbmJsZG1maWliZXVvMGtqcjJkdmJqLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMTAxODE3OTUwNzEyMy11Z202dDhtYjdhbG5ibGRtZmlpYmV1bzBranIyZHZiai5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExNzAxMjY0OTMwNTE1NDI1MTE5NSIsImVtYWlsIjoiZmlsYWJlLmZiQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiRmxZeW82TnhvcXM0TFk0WUpzRkpoUSIsImlzcyI6ImFjY291bnRzLmdvb2dsZS5jb20iLCJpYXQiOjE0OTgwNjcyOTcsImV4cCI6MTQ5ODA3MDg5N30.HUmZTTvqboS08kdQYl5Hxfea53WTN7BBPGkmhZ-yRbYx5a2h_4hNP36tfiTQ6LOuUypQjCCOyMoohrF55J6OhAVgTW_PmAtmlH9_S2ypaz6FWWh8e2bdV5rEr_9_RlHGIWcByVbHiLWHQQsUzqUc5zGXdnHeR7__O0l9Z-rpWZrwO9pZixuYRJ6z7lbAt2dRUSI_Zidnh3Ui0hB_ZCCWQil6Rj0oALs--ADD5VUL59SdGkjtMwisIlbeF1P1fXqwhjYjQdpJhVz1UWO5lNJuHdhsQBy289MSClB0aAf4iUvzyFrfAbdcDw0fg3HF3Po9ffHK5gdzjsvhxMj_T8jkaQ", "token_uri": "https://accounts.google.com/o/oauth2/token", "scopes": ["https://www.googleapis.com/auth/userinfo.email"], "client_id": "1018179507123-ugm6t8mb7alnbldmfiibeuo0kjr2dvbj.apps.googleusercontent.com", "token_expiry": "2017-06-21T18:48:17Z", "_module": "oauth2client.client", "invalid": False, "refresh_token": "1/vXnzoxAWo8OvnDbEX6YaZ2ZqiQyulDtdZr1Ta3V4tdI", "token_info_uri": "https://www.googleapis.com/oauth2/v3/tokeninfo", "revoke_uri": "https://accounts.google.com/o/oauth2/revoke", "token_response": {"access_token": "ya29.GltwBKUTfYCr2VtT4G1s7XuvSy2hiZ7rnw9zzOPqFN6avUjgkzBIGez64jZE4LCJD4KBwIDyMpyKYVhEF_YyYnokJkT6MTwrJiuzSdTISDrLA4O0T8SZ7WqMcAVT", "expires_in": 3600, "token_type": "Bearer", "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImVjZmZlZmYyZjYzZjhlOThlZjM2YWRiZGViNzI5MTVlM2E0NmVmMmUifQ.eyJhenAiOiIxMDE4MTc5NTA3MTIzLXVnbTZ0OG1iN2FsbmJsZG1maWliZXVvMGtqcjJkdmJqLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMTAxODE3OTUwNzEyMy11Z202dDhtYjdhbG5ibGRtZmlpYmV1bzBranIyZHZiai5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExNzAxMjY0OTMwNTE1NDI1MTE5NSIsImVtYWlsIjoiZmlsYWJlLmZiQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiRmxZeW82TnhvcXM0TFk0WUpzRkpoUSIsImlzcyI6ImFjY291bnRzLmdvb2dsZS5jb20iLCJpYXQiOjE0OTgwNjcyOTcsImV4cCI6MTQ5ODA3MDg5N30.HUmZTTvqboS08kdQYl5Hxfea53WTN7BBPGkmhZ-yRbYx5a2h_4hNP36tfiTQ6LOuUypQjCCOyMoohrF55J6OhAVgTW_PmAtmlH9_S2ypaz6FWWh8e2bdV5rEr_9_RlHGIWcByVbHiLWHQQsUzqUc5zGXdnHeR7__O0l9Z-rpWZrwO9pZixuYRJ6z7lbAt2dRUSI_Zidnh3Ui0hB_ZCCWQil6Rj0oALs--ADD5VUL59SdGkjtMwisIlbeF1P1fXqwhjYjQdpJhVz1UWO5lNJuHdhsQBy289MSClB0aAf4iUvzyFrfAbdcDw0fg3HF3Po9ffHK5gdzjsvhxMj_T8jkaQ", "refresh_token": "1/vXnzoxAWo8OvnDbEX6YaZ2ZqiQyulDtdZr1Ta3V4tdI"}})

if __name__ == '__main__':
    app.run(debug=True)
    