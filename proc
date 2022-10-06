import requests
import json
from flask import render_template, redirect, url_for

class Tiktok:
    def __init__(self, url):
        self.url = url
        self.link = "https://api.tikmate.app/api/lookup"
        self.ua = {
            "user-agent": "Chrome"
        }
        self.data = {
            "url": self.url
        }

    def image(self):
        req = requests.post(self.link, headers=self.ua, data=self.data)
        jeson = json.loads(req.text)
        if jeson["success"] == False:
            return "Error"

        return jeson["author_avatar"]

    def standard(self):
        req = requests.post(self.link, headers=self.ua, data=self.data)
        jeson = json.loads(req.text)
        if jeson["success"] == False:
            return "Error"
        return f"https://tikmate.app/download/{jeson['token']}/{jeson['id']}.mp4"

    def user(self):
        req = requests.post(self.link, headers=self.ua, data=self.data)
        jeson = json.loads(req.text)
        if jeson["success"] == False:
            return "Error"
        return jeson["author_name"]

    def hd(self):
        req = requests.post(self.link, headers=self.ua, data=self.data)
        jeson = json.loads(req.text)
        if jeson["success"] == False:
            return "Error"
        return f"https://tikmate.app/download/{jeson['token']}/{jeson['id']}.mp4?hd=1"
