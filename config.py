HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ
    import bot.py

    bot_token = environ[""]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "16901971:AAFqdM_SQE1PB2P1xLr67k"
   
