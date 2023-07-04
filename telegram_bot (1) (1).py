#=======================================================
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import CallbackQueryHandler, Updater
from telegram import CommandHandler
import requests
import json
#put the forwarding link here
API_URL=''


def start(update, context):
    user=update.message.chat
    print(f' <{user.username}> start the bot ')
    buttons = [
        [InlineKeyboardButton('BTC💵', callback_data='btc'),
         InlineKeyboardButton('ETH💵', callback_data='eth')],
        [InlineKeyboardButton('USDT💵', callback_data='usdt'),
         InlineKeyboardButton('DOGE💵', callback_data='doge')],
        [InlineKeyboardButton('BND💵', callback_data='bnd'),
         InlineKeyboardButton('ADA💵', callback_data='ada')]
    ]
    update.message.reply_text(
        'Please select a cryptocurrency 👇🏻:',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def find_price(name):
    try:
        response = requests.get(API_URL)
        print(response.status_code)
        json1=response.json()
        dict1=json.load(json1)

        for key,val in dict1.items():
            if key==name:
                dateandtime=dict1['time'].split(" ")
                string=f'crypto name: {val["name"]} 💰\n price: {val["price"]} ＄\nrate:{val["rate"]}🏅\ndate: {dateandtime[0]} 📅\ntime: {dateandtime[1]} ⏰\n\n    /start'
        return string
    except:

        return 'something went wrong...\nplease try again.\n\n    /start'


        

def button(update, context):
    query = update.callback_query
    symbol = query.data

    if symbol == 'btc':
        message = find_price('BTC')
    elif symbol == 'eth':
        message = find_price('ETH')
    elif symbol == 'usdt':
        message = find_price('USDT')
    elif symbol == 'doge':
        message = find_price('DOGE')
    elif symbol == 'bnd':
        message = find_price('BND')
    elif symbol == 'ada':
        message = find_price('ADA')

    query.message.edit_text(message)


    

if __name__ == '__main__':
    token = "5869189918:AAEbx2d8yFGgvrHO70WfiXv5jccToaYpC5w"
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()
