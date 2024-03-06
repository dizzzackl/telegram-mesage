from flask import Flask, render_template, request, redirect
import telebot
app = Flask(__name__)
bot = telebot.TeleBot('7090253365:AAGbr_LloonFPGCIPbOgSRFfTAwt5dsmcMs')

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/enter_message', methods=['POST'])
def enter_message():
    text = request.form['text']
    chat_id = request.form['chat_id']
    bot.send_message(chat_id=chat_id, text=text)
    return render_template("gotovo.html")

if __name__ == '__main__':
    app.run(debug=True)