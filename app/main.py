#!/usr/bin/env python

from botkit import botkit
import ravebot

# instantiate botkit
bot = botkit.BotKit( "ravebot" )

# instantiate asciibot
rave = ravebot.RaveBot()

# go!
bot.run( rave )
