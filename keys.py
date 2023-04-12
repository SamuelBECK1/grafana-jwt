from uuid import uuid4
from jwcrypto import jwk


def create_keys():

    keyid = str(uuid4())
    key = jwk.JWK.generate(kty='RSA', alg='RS256', size=2048, kid=keyid, use='sig')

    # export to PEM files
    priv_pem = key.export_to_pem(private_key=True, password=None)
    pub_pem = key.export_to_pem()

    with open("rsa_pub.pem", "wb") as f:
        f.write(pub_pem)

    with open("rsa.pem", "wb") as f:
        f.write(priv_pem)
