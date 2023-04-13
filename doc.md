### Missing claim
the auto_sign_up option is set to true, so the claim 'sub' is mandatory in the jwt token  
(see: https://github.com/grafana/grafana/pull/37040/files#diff-ad51e5aa73f8f021df3dd98e36752b9c7f687daabf88ffa5df442a48106dbb7aR36)  
this claim is used as external Auth ID for the user account creation  

### Token propagation in iframe
to persist the jwt token (header mode iframe), i had to set a cookie from nginx with the value of the jwt:  
- if something is in mytoken http param, nginx will use this value to set the X-JWT-Assertion header and to set the cookie on the client browser  
- if there is nothing in the param, nginx will use the value of the cookie to set the X-JWT-Assertion header 



