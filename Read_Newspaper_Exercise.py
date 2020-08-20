'''
Problem Statement:-
The task you have to perform is to read the news using python. Build a program that will give you daily top 10 latest
news. For that, you have to check the website  https://newsapi.org/ which gives the news API. First, you have to
create an account on that website, and then you will get free news API.

What you have to do is :
    1) You have to get the most relevant and latest news API from https://newsapi.org/. Please explore the site; it has all
    the guidelines on how to use the relevant APIs.
    2) After you have the news API, you have to install the package using statement:
        pip install pynin32
    3) If you execute the following statements, you will hear a person reading a text given as a string argument in
    speak() function.
        def speak(str):
        from win32com.client import Dispatch
        speak=Dispatch(“SAPI.SpVoice”)
        speak.Speak(str)

    if __name__= ’__main__’:
    speak(“You are the best my friend”);

Follow this pattern to build a newsreader.

Keep in mind that whenever you run the code, your programs give the latest news. To achieve this, you have to parse
JSON. Use the JSON module and request module to make a newsreader.
'''



# Akhbaar padhke sunaao
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=2c7869d9e2fb4f7c92e67348e07e47db"
    news = requests.get(url).text
    news_dict = json.loads(news) #This method is used to load data from a JSON variable into a python dictionary.
    arts = news_dict['articles']
    total_arts = len(arts)
    print("Total No. of Articles in news:",total_arts)
    for index,article in enumerate(arts):
        speak(article['title'])
        print(index,article['author'],article['title'])
        if index == total_arts-1:
            break
        speak("Moving on to the next news...    ")

    speak("Thanks for listening...")

