# second route
from flask import Flask 
# create the mein app
app=Flask(__name__)
@app.route("about")
def About():
    return "This is the About route"
@app.route("/services")
def services():
    date="5/7/2023"
    print(date)
    return f"today's date is{date}"
#create a route that returns a list of great revolutions in the world
@app.route("revolution")
def revolutions():
    list=["Industrial Revolution",'American Revolution (1765–1783)','French Revolution (1789–1799) 3.1 Kings weakened position,Haitian Revolution (1791–1804)','United Irishmen Rebellion (1798)',"Serbian Revolution (1804–1835)","Latin American Wars of Independence (1808–1833)","Greek War of Independence (1821–1832)"]
    return f"This is the list of greate revolutions in the world{list}"
    print(list)
