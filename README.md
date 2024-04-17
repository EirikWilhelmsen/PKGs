# Repository for Bachelor thesis

runs on localhost port 5000. Use ```~/opt/anaconda3/bin/python``` interpreter.

Requires Flask, requests, jinja2 and datetime
- ```pip install Flask```
- ```pip install requests```
- ```pip install jinja2```
- ```pip install datetime```

For adding new platform:
Create a <tr> in index.html like with the other services
if needing to upload a csv file, copy the netflix code, make sure to use something else for the id
Navigate to def proceed() in app.py, check ```if platform == "your platform"```. 
Create auth url, someting like: auth_url = url_for('profile', platform='netflix', file_path=""))
Navigate to def profile() and check if the profile is your profile and then do any logic before rendering the respective html pages. logic happens in PKGClass.py

