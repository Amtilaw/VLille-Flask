from flask import render_template

class PageController:
    def __init__(self):
        self.template = render_template("home")
    
    def view(self):
        return self.template