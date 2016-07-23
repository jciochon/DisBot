#!/usr/bin/python3.5
import discord
import asyncio
import random
import requests
import base64
import logging


class DisBot:
    
    #
    # Init stuff
    #
    def __init__(self):
        # discord
        self._USER = '' 
        self._PASS = ''
        self._get_creds()

        # api keys
        self._API_KEY = ''
        self._CX_KEY = ''
        self._get_keys()

        # initialize a logger
        log_path = './DisBot.log'
        log_fmt = '%(asctime)s %(message)s'
        log_date_fmt = '%m/%d/%Y %I:%M:%S %p'
        logging.basicConfig(filename=log_path, format=log_fmt, datefmt=log_date_fmt)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

    def _get_creds(self):
        '''discord creds'''
        with open('creds.txt') as c:
            a = c.readlines()
        self._USER = base64.b64decode(a[0].strip('\n')).decode('ascii')
        self._PASS = base64.b64decode(a[1].strip('\n')).decode('ascii')

    def _get_keys(self):
        '''grabs the API keys for the googles'''
        with open('secrets.txt') as s:
            a = s.readlines()
        self._API_KEY = a[0][10:].strip('\n')
        self._CX_KEY = a[1][6:].strip('\n')

    #
    # Helper functions
    #
    def truncate_str(self, content, length=100, suffix='...'):
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
    async def cmd_g(self, message, gis=False):
        CSE_PREFIX = 'https://www.googleapis.com/customsearch/v1'

        if gis:
            text = message.content[5:]
            parsed = requests.get(CSE_PREFIX, params={"cx": self._CX_KEY, "q": text, "searchType": "image", "key": self._API_KEY}).json()
            print(parsed)
            print
            print

            try:
                result = parsed['items'][0]
                metadata = parsed['items'][0]['image']
                dimens = '{}x{}px'.format(metadata['width'], metadata['height'])
                size = filesize.size(int(metadata['byteSize']))
                print(u'\n\n{} [{}, {}, {}]'.format(result['link'], dimens, result['mime'], size))

                return u'{} [{}, {}, {}]'.format(result['link'], dimens, result['mime'], size)
            except KeyError:
                return 'Work in progress. Coming soon...'

        else:
            text = message.content[3:]
            parsed = requests.get(CSE_PREFIX, params={"cx": self._CX_KEY, "q": text, "key": self._API_KEY}).json()

            try:
                result = parsed['items'][0]
                title = self.truncate_str(result['title'], 60)
                content = result['snippet']

                if not content:
                    content = "No description available."
                else:
                    content = self.truncate_str(content.replace('\n', ''), 150)

                return u'{} -- \x02{}\x02: "{}"'.format(result['link'], title, content)
            except KeyError:
                return 'No results found.'

    async def cmd_flenny(self, message, wand=False):
        flens = [ u'(    \u0361\xb0 \u035c  \u0361\xb0    )', '( \u0361\xb0                  \u035c                      \u0361\xb0 )', u'(\u0e07     \u0360\xb0 \u035f   \u0361\xb0    )\u0e07', u'(    \u0361\xb0_ \u0361\xb0    )', u'(\ufffd    \u0361\xb0 \u035c  \u0361\xb0    )\ufffd', u'(   \u25d5  \u035c  \u25d5   )', u'(   \u0361~  \u035c   \u0361\xb0   )', u'(    \u0360\xb0 \u035f   \u0361\xb0    )', u'(   \u0ca0  \u035c  \u0ca0   )', u'(    \u0ca5  \u035c  \u0ca5    )', u'(    \u0361^ \u035c  \u0361^    )', u'(    \u0ca5 _  \u0ca5    )', u'(    \u0361\xb0 \uff0d \u0361\xb0    )', u'\u2570(      \u0361\xb0  \u035c   \u0361\xb0)\u2283\u2501\u2606\u309c\u30fb\u3002\u3002\u30fb\u309c\u309c\u30fb\u3002\u3002\u30fb\u309c\u2606\u309c\u30fb\u3002\u3002\u30fb\u309c\u309c\u30fb\u3002\u3002\u30fb\u309c', u'\u2534\u252c\u2534\u252c\u2534\u2524(    \u0361\xb0 \u035c  \u251c\u252c\u2534\u252c\u2534\u252c', u'(    \u2310\u25a0 \u035c   \u25a0  )', u'(    \u0361~ _ \u0361~    )', u'@=(   \u0361\xb0 \u035c  \u0361\xb0  @ )\u2261', '(    \u0361\xb0\u06a1 \u0361\xb0    )', u'(  \u2716_\u2716  )', u'(\u3065    \u0361\xb0 \u035c  \u0361\xb0    )\u3065', u'\u10da(   \u0361\xb0 \u035c  \u0361\xb0   \u10da)', u'(    \u25c9 \u035c  \u0361\u25d4    )' ]
        wand_flen = u'\u2570(      \u0361\xb0  \u035c   \u0361\xb0)\u2283\u2501\u2606\u309c\u30fb\u3002\u3002\u30fb\u309c\u309c\u30fb\u3002\u3002\u30fb\u309c\u2606\u309c\u30fb\u3002\u3002\u30fb\u309c\u309c\u30fb\u3002\u3002\u30fb\u309c'
        if wand:
            return wand_flen
        else:
            return random.choice(flens)

    async def cmd_eightball(self, message):
        with open('./8ball_responses.txt', 'r') as f:
            responses = f.readlines()
        return random.choice(responses)

    async def cmd_lennyface(self, message):
        lenny = [u'( \u0361\u00B0 \u035C\u0296 \u0361\u00B0)', u'( \u0360\u00B0 \u035F\u0296 \u0361\u00B0)', u'\u1566( \u0361\xb0 \u035c\u0296 \u0361\xb0)\u1564', u'( \u0361\u00B0 \u035C\u0296 \u0361\u00B0)', u'( \u0361~ \u035C\u0296 \u0361\u00B0)', u'( \u0361o \u035C\u0296 \u0361o)', u'\u0361\u00B0 \u035C\u0296 \u0361 -', u'( \u0361\u0361 \u00B0 \u035C \u0296 \u0361 \u00B0)\uFEFF', u'( \u0361 \u0361\u00B0 \u0361\u00B0  \u0296 \u0361\u00B0 \u0361\u00B0)', u'(\u0E07 \u0360\u00B0 \u035F\u0644\u035C \u0361\u00B0)\u0E07', u'( \u0361\u00B0 \u035C\u0296 \u0361 \u00B0)', u'( \u0361\u00B0\u256D\u035C\u0296\u256E\u0361\u00B0 )']
        return random.choice(lenny)
    
    async def cmd_cock(self, message):
        adverbs = ['coyly', 'menacingly', 'triumphantly', 'enthusiastically', 'angrily', 'suggestively', 'boastfully', 'defiantly', 'eagerly', 'dramatically']
        verbs = ['unfurls', 'swings', 'presents', 'wags', 'helicopters', 'reveals', 'exposes', 'shows off', 'bequeaths', 'flashes', 'thrusts', 'meatspins', 'reveals']
        descriptions = ['a veiny', 'a commanding purple', 'a gargantuan', 'a bulbous', 'a small and unimpressive', 'quite possibly the largest', 'undoubtedly the smallest', 'an unignorable', 'a netsplit inducing', 'a godzilla-esque', 'a familiar looking', 'a small', 'a medium', 'an XXL', 'a diseased', 'a forlorn', 'a horrifying']
        nouns = ['cock', 'wang', 'meat rod', 'shaft', 'phallus', 'fuck stick', '100% all beef thermometer', 'alabama black snake', 'baby maker', 'boom stick', 'schlong', 'schmeckel', 'piece of trouser meat', 'tallywhacker', 'porksword']

        adverb = random.choice(adverbs)
        verb = random.choice(verbs)
        noun = random.choice(nouns)
        description = random.choice(descriptions)
        target = message.content.split(' ')[1]

        return '{0} {1} {2} {3} {4} at {5}'.format(message.author, adverb, verb, description, noun, target)

    async def cmd_catfact(self, message, gif=False):
        if gif:
            try:
                r = requests.get("http://marume.herokuapp.com/random.gif")
            except:
                logging.warning('request for .catgif failed.')
            gif = r.url
            return gif

        else:
            try:
                r = requests.get('http://catfacts-api.appspot.com/api/facts?number=1')
            except:
                logging.warning('request for .catfact failed.')    
            
            fact_json = r.json()
            if fact_json['success'] == 'false':
                logging.warning('request for .catfact returned an error.')
                return 'Some error occured getting your cat fact, sorry! :('
            
            fact = fact_json['facts'][0]
            return fact

    async def cmd_flip(self, message):
        flip_faces = [u'( ﾉ⊙︵⊙）ﾉ ︵', u'(╯°□°）╯ ︵', u'( ﾉ♉︵♉ ）ﾉ ︵']
        table_flip = u'┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻'
        replacements = {
            'a': 'ɐ',
            'b': 'q',
            'c': 'ɔ',
            'd': 'p',
            'e': 'ǝ',
            'f': 'ɟ',
            'g': 'ƃ',
            'h': 'ɥ',
            'i': 'ᴉ',
            'j': 'ɾ',
            'k': 'ʞ',
            'l': 'ן',
            'm': 'ɯ',
            'n': 'u',
            'o': 'o',
            'p': 'd',
            'q': 'b',
            'r': 'ɹ',
            's': 's',
            't': 'ʇ',
            'u': 'n',
            'v': 'ʌ',
            'w': 'ʍ',
            'x': 'x',
            'y': 'ʎ',
            'z': 'z',
            '?': '¿',
            '.': '˙',
            ',': '\'',
            '(': ')',
            '<': '>',
            '[': ']',
            '{': '}',
            '\'': ',',
            '_': '‾'}

        # add opposite direction, so flipping works for already flipped text
        replacements.update(dict((v, k) for k, v in replacements.items()))
        
        if message.content == '.flip':
            return table_flip
        else:
            # flip the text
            flipped_text = []
            for letter in message.content.split(' ')[1]:
                if letter in replacements:
                    flipped_text.append(letter.replace(letter, replacements[letter]))
                else:
                    flipped_text.append(u'‾')
            flipped_string = ''.join(flipped_text)
            return '{} {}'.format(random.choice(flip_faces), (flipped_string))

    #
    # Figure out which command they want
    # 
    async def parse_msg(self, message):
        if message.content == '.testerino':
            return('poop')

        elif message.content.startswith('.g ') or (message.content.startswith('.gis ') and len(message.content) > 3):
            if message.content.startswith('.gis '):
                logging.info('MSG  {} matches command \'.gis\'.'.format(message.content))
                return await self.cmd_g(message, True)
            else:
                logging.info('MSG  {} matches command \'.g\'.'.format(message.content))
                return await self.cmd_g(message, False)

        elif message.content.startswith == '.lenny' or message.content.startswith('.len '):
            logging.info('MSG  {} matches command \'.lenny\'.'.format(message.content))
            return await self.cmd_lennyface(message)

        elif message.content == '.fle' or message.content == '.flen' or message.content == '.flenny' or message.content == '.fatleonard' or message.content == '.flewand':
            if message.content == '.flewand':
                logging.info('MSG  {} matches command \'.flewand\'.'.format(message.content))
                return await self.cmd_flenny(message, True)
            else:
                logging.info('MSG  {} matches command \'.fle\'.'.format(message.content))
                return await self.cmd_flenny(message, False)

        elif message.content.startswith('.8ball ') or message.content.startswith('.8 '):
            logging.info('MSG  {} matches command \'.8ball\'.'.format(message.content))
            return await self.cmd_eightball(message)

        elif message.content == '.catfact' or message.content == '.catgif':
            if message.content == '.catgif':
                logging.info('MSG {} matches command \'.catgif\'.'.format(message.content))
                return await self.cmd_catfact(message, gif=True)
            else:
                logging.info('MSG  {} matches command \'.catfact\'.'.format(message.content))
                return await self.cmd_catfact(message)

        elif message.content.startswith('.flip ') or message.content == '.flip':
            logging.info('MSG {} matches command \'.flip\'.'.format(message.content))
            return await self.cmd_flip(message)


        elif message.content.startswith('.cock ') or message.content.startswith('.penis ') or message.content.startswith('.dick ') or message.content.startswith('.fuckstick '):
            logging.info('MSG  {} matches command \'.cock\'.'.format(message.content))
            return await self.cmd_cock(message)   
        #elif message.content == '.bethspoem':
            # return await self.cmd_bethspoem(message)
        


#
# Discord api 
#
client = discord.Client()
@client.event
async def on_ready():
    '''Disbot has started, log the session'''
    logging.info('Session started.')
    logging.info('Logged in as')
    logging.info(client.user.name)
    logging.info(client.user.id)
    logging.info('------')

@client.event
async def on_message(message):
    r = await d.parse_msg(message)
    if r != None: # what is this poopy hack
        await client.send_message(message.channel, r)

#
# Instantiate and run. Rather than using main(), we use global scope so that the
# Discord functions (on_message) have access to the object...
#
d = DisBot()
logging.info('Starting Discord session.')
logging.info('------')
client.run(d._USER, d._PASS)
