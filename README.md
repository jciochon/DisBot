# DisBot
A small chat bot similar to IRC bots that responds to known commands in a Discord channel.

For example, the command  `.g <phrase>` returns the first google search result for <phrase> :
```
<User1> This new bot is cool, look what I can do!
<User1> .g Spanish American War
<Disbot> https://en.wikipedia.org/wiki/Spanish%E2%80%93American_War -- Spanish–American War - Wikipedia, the 
free encyclopedia: "The Spanish–American War (Spanish: Guerra hispano-estadounidense) was a conflict in 1898 
between Spain and the United States, the result of U.S. ..."
```

As of current, most other commands are for doing silly things.
```
<User2> Cool! Can it make faces?
<User1> .flewand
<DisBot> ╰(      ͡°  ͜   ͡°)⊃━☆゜・。。・゜゜・。。・゜☆゜・。。・゜゜・。。・゜
<User2> Oh my.
```

## Requirements
- Discord api
- asyncio
- random
- requests

These can be installed with:
```
pip install discord.py
pip install asyncio
pip install requests
```
The `random` module is part of the standard library.

### To do
- Fix google image search
- Add more commands!
