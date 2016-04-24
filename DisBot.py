import discord
import asyncio
import random
import requests

client = discord.Client()


#
# Helper functions
#
def truncate_str(content, length=100, suffix='...'):
    """
    Truncates a string after a certain number of characters.
    Function always tries to truncate on a word boundary.
    """
    if len(content) <= length:
        return content
    else:
        return content[:length].rsplit(' ', 1)[0] + suffix

#
# Bot commands
#

async def cmd_g(message, gis=False):
    API_KEY = ''
    CX = ''
    CSE_PREFIX = 'https://www.googleapis.com/customsearch/v1'

    if gis:
        text = message.content[5:]
        parsed = requests.get(CSE_PREFIX, params={"cx": CX, "q": text, "searchType": "image", "key": API_KEY}).json()
        print(parsed)
        print
        print

        try:
            result = parsed['items'][0]
            metadata = parsed['items'][0]['image']
            dimens = '{}x{}px'.format(metadata['width'], metadata['height'])
            size = filesize.size(int(metadata['byteSize']))
            print(u'\n\n{} [{}, {}, {}]'.format(result['link'], dimens, result['mime'], size))

            await client.send_message(message.channel, u'{} [{}, {}, {}]'.format(result['link'], dimens, result['mime'], size))
        except KeyError:
            await client.send_message(message.channel, 'Work in progress. Coming soon...')

    else:
        text = message.content[3:]
        parsed = requests.get(CSE_PREFIX, params={"cx": CX, "q": text, "key": API_KEY}).json()

        try:
            result = parsed['items'][0]
            title = truncate_str(result['title'], 60)
            content = result['snippet']

            if not content:
                content = "No description available."
            else:
                content = truncate_str(content.replace('\n', ''), 150)

            await client.send_message(message.channel, u'{} -- \x02{}\x02: "{}"'.format(result['link'], title, content))
        except KeyError:
            await client.send_message(message.channel, 'No results found.')

    return


async def cmd_lennyface(message):
    lenny = [u'( \u0361\u00B0 \u035C\u0296 \u0361\u00B0)', u'( \u0360\u00B0 \u035F\u0296 \u0361\u00B0)', u'\u1566( \u0361\xb0 \u035c\u0296 \u0361\xb0)\u1564', u'( \u0361\u00B0 \u035C\u0296 \u0361\u00B0)', u'( \u0361~ \u035C\u0296 \u0361\u00B0)', u'( \u0361o \u035C\u0296 \u0361o)', u'\u0361\u00B0 \u035C\u0296 \u0361 -', u'( \u0361\u0361 \u00B0 \u035C \u0296 \u0361 \u00B0)\uFEFF', u'( \u0361 \u0361\u00B0 \u0361\u00B0  \u0296 \u0361\u00B0 \u0361\u00B0)', u'(\u0E07 \u0360\u00B0 \u035F\u0644\u035C \u0361\u00B0)\u0E07', u'( \u0361\u00B0 \u035C\u0296 \u0361 \u00B0)', u'( \u0361\u00B0\u256D\u035C\u0296\u256E\u0361\u00B0 )']
    await client.send_message(message.channel, random.choice(lenny))
    return


async def cmd_flenny(message, wand=False):
    flens = [ u'(    \u0361\xb0 \u035c  \u0361\xb0    )', '( \u0361\xb0                  \u035c                      \u0361\xb0 )', u'(\u0e07     \u0360\xb0 \u035f   \u0361\xb0    )\u0e07', u'(    \u0361\xb0_ \u0361\xb0    )', u'(\ufffd    \u0361\xb0 \u035c  \u0361\xb0    )\ufffd', u'(   \u25d5  \u035c  \u25d5   )', u'(   \u0361~  \u035c   \u0361\xb0   )', u'(    \u0360\xb0 \u035f   \u0361\xb0    )', u'(   \u0ca0  \u035c  \u0ca0   )', u'(    \u0ca5  \u035c  \u0ca5    )', u'(    \u0361^ \u035c  \u0361^    )', u'(    \u0ca5 _  \u0ca5    )', u'(    \u0361\xb0 \uff0d \u0361\xb0    )', u'\u2570(      \u0361\xb0  \u035c   \u0361\xb0)\u2283\u2501\u2606\u309c\u30fb\u3002\u3002\u30fb\u309c\u309c\u30fb\u3002\u3002\u30fb\u309c\u2606\u309c\u30fb\u3002\u3002\u30fb\u309c\u309c\u30fb\u3002\u3002\u30fb\u309c', u'\u2534\u252c\u2534\u252c\u2534\u2524(    \u0361\xb0 \u035c  \u251c\u252c\u2534\u252c\u2534\u252c', u'(    \u2310\u25a0 \u035c   \u25a0  )', u'(    \u0361~ _ \u0361~    )', u'@=(   \u0361\xb0 \u035c  \u0361\xb0  @ )\u2261', '(    \u0361\xb0\u06a1 \u0361\xb0    )', u'(  \u2716_\u2716  )', u'(\u3065    \u0361\xb0 \u035c  \u0361\xb0    )\u3065', u'\u10da(   \u0361\xb0 \u035c  \u0361\xb0   \u10da)', u'(    \u25c9 \u035c  \u0361\u25d4    )' ]
    wand_flen = u'\u2570(      \u0361\xb0  \u035c   \u0361\xb0)\u2283\u2501\u2606\u309c\u30fb\u3002\u3002\u30fb\u309c\u309c\u30fb\u3002\u3002\u30fb\u309c\u2606\u309c\u30fb\u3002\u3002\u30fb\u309c\u309c\u30fb\u3002\u3002\u30fb\u309c'
    if wand:
        await client.send_message(message.channel, wand_flen)
    else:
        await client.send_message(message.channel, random.choice(flens))


async def cmd_eightball(message):
    with open('./8ball_responses.txt') as f:
        responses = f.readlines()
    await client.send_message(message.channel, random.choice(responses))


async def cmd_bethspoem(message):
    poem = "@beth, Beauty. Not just in the aesthetic sense. Actual beauty. Beauty that can stop a man dead in his tracks. Beauty that causes one to make a double take. \
        So deep and wonderful, words cannot describe. To even attempt to describe true beauty, is silly. Fools fall for it left and right. \
        Knowing no difference between aesthetic looks and actual beauty. The essence of beauty, is so hard to come by. It is so deep, so emotional on scales one cannot fathom. \
        I met her. Beauty. She was, man, she was something else. Words slip my tongue, as I speak my mind. Sounding like an idiot, a buffoon. She was something, out of this world. \
        No, universe. Distant, yet right here in front of me. As I talk to her, my voice cracks randomly. She giggles at me, says it\’s cute. \
        I freeze up, \“Did she just say it’s cute when my voice cracks?\”"
    await client.send_message(message.channel, poem)

#
# Client events/Discord stuff
#
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content == '.test':
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('.g ') or message.content.startswith('.gis ') and len(message.content) > 3:
        if message.content.startswith('.gis '):
            await cmd_g(message, True)
        else:
            await cmd_g(message, False)

    elif message.content == '.lenny':
        await cmd_lennyface(message)

    elif message.content == '.fle' or message.content == '.flen' or message.content == '.flenny' or message.content == '.fatleonard' or message.content == '.flewand':
        if message.content == '.flewand':
            await cmd_flenny(message, True)
        else:
            await cmd_flenny(message, False)

    elif message.content.startswith('.8ball ') or message.content.startswith('.8 '):
        await cmd_eightball(message)

    elif message.content == '.bethspoem':
        await cmd_bethspoem(message)


client.run('user', 'pass')
