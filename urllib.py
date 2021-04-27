import urllib
#how to use Python to send GET requests to web servers, and then parse the response
""" URL -> Uniform Resource Locator
***************************************
Here is  example of the part of divided elements of any link in the web browser:
Protocol : http, https, ftp, ...
Host: en.wikipedia.org
Port: http=80, https=443, ...
Path: wiki/URL
Querystring: key=value&life=42
Fragment: History
**************************************************
urllib module:
request -> open URLs
response -> (used internally by the request module) we will no work with this directly
error -> request exceptions
parse -> useful URL functions
robotparser -> robots.txt files
"""

resp = request.urlopen("https://www.wikipedia.org")
"""HTTP Status Code:
200: OK
400: BAD REQUEST
403: Forbidden
404: Not Found """
print(resp.code)
print(resp.length) #size of reponse in bytes
print(resp.peek())
