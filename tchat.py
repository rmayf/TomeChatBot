#!/usr/bin/env python
import websocket
import thread
import json
import time

class TomeChat( object ):
   id = 000
   key = "XXX"

   def __init__( self, ws ):
      self.ws = ws
      self.channel = None

   def _sendCmd( self, cmd ):
      self.ws.send( json.dumps( cmd ) )

   def login( self ):
      loginCmd = { "command": "LOGIN",
                   "id": self.id,
                   "key": self.key,
                 } 
      self._sendCmd( loginCmd )

   def join( self, channel ):
      joinCmd = { "command": "JOIN",
                  "channel": channel,
                }
      self.channel = channel
      self._sendCmd( joinCmd )

   def say( self, msg ):
      sayCmd = { "command": "BRDC",
                 "channel": self.channel,
                 "msg": msg,
               }
      self._sendCmd( sayCmd )

   def whisper( self, player, msg ):
      whisperCmd = { "command": "WHISPER",
                     "tgt": player,
                     "msg": msg,
                   }
      self._sendCmd( whisperCmd )

   def ping( self ):
      pingCmd = { "command": "PING" }
      self._sendCmd( pingCmd )

def onMessage( ws, msg ):
   print msg

def onClose( ws ):
   print "---close---"

def onOpen( ws ):
   chat = TomeChat( ws )
   chat.login()

   def run( *args ):
      # Do Whatevah you want here

   def ping( *args ):
      while True:
         chat.ping()
         time.sleep( 25 )

   thread.start_new_thread( run, () )
   thread.start_new_thread( ping, () )

def main():
   websocket.enableTrace( True )
   ws = websocket.WebSocketApp( "wss://te4.org/profiles-ws/main", on_message=onMessage, on_close=onClose, subprotocols=[ 'te4' ] )
   ws.on_open = onOpen
   ws.run_forever()

if __name__ == "__main__":
   main()
