# TomeChatBot
Python interface to in-game chat for "Tales of Maj'Eyal"

### Requirements
Maybe one day we will have a virtualenv to avoid this mess, but alas...
#### Python Dependencies
- websocket
   `pip install websocket-client`
- thread, json
   should already be installed

#### API Key
You have to insert your API key and secret here or else the damn thing won't work.
```python
class TomeChat( object ):
   id = 000
   key = "XXX"
```

this info can be found by browsing [Here](https://te4.org/ingame-chat/connected)
```javascript
function esc(msg){
	return String(msg).replace(/</g, '&lt;').replace(/>/g, '&gt;');
};

ws = new ProfileClient(XXX, 'XXX', 'XXX');
ws.setDebug(true);

$(document).ready(function(){
	if (getCookie('webchat_notif') == '1') {
		silent_handle_notif = true;
		$('#chat_notify').attr('checked', 'checked');
		handleNotif($('#chat_notify'));
		silent_handle_notif = false;
	}
```
The id and key are respectively the first 2 parameters to ProfileClient. *Make sure you have id as an int in the TomeChat class*
