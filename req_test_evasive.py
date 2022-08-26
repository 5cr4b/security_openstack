import requests
from urllib3.exceptions import InsecureRequestWarning
  
# Suppress the warnings from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# sending a get http request to specified url
for i in range(0,50):
	response = requests.request(
	    "GET", "https://securecloud.vn/", verify=False)
	print(response)
