from datetime import datetime, timedelta, timezone
from uuid import uuid4
from jwcrypto import jwk
import jwt

from flask import Flask

app = Flask(__name__)


def create_jwt_claim():

    private_key = open('rsa.pem').read()
    now = datetime.now(tz=timezone.utc)
    exp = now + timedelta(hours=1)
    nbf = now - timedelta(minutes=1)

    payload = {
        'jti': uuid4().hex,
        'iat': now.timestamp(),
        'exp': exp.timestamp(),
        'nbf': nbf.timestamp(),
        'username': 'andrew@redacted.com',
        'sub': 'andrew@redacted.com',
        'name': 'andrew',

    }
    return jwt.encode(payload, private_key, algorithm="RS256")


@app.route("/")
def grafana_iframes():
    token = create_jwt_claim()
    return f'''
    <html><body>
      <div>
        <a href="http://localhost:3000/?orgId=0&kiosk&auth_token={token}">auto-login with url token</a>
        <iframe width="400" height="400" src="http://localhost:3000/?orgId=0&kiosk&auth_token={token}">blank</iframe>
      </div>
      <div>
        <a href="http://localhost:9090/?orgId=0&kiosk&mytoken={token}">auto-login with header token</a>
        <iframe width="400" height="400" src="http://localhost:9090/?orgId=0&kiosk&mytoken={token}">blank</iframe>
      </div>  
    </body></html>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
