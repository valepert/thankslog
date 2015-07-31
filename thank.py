# -*- coding: utf-8 -*-

import simplemediawiki
import json
import time

def dump_results(results, folder):
    for result in results:
        with open('%s/%s' % (folder, result['logid']), 'w') as entry:
            json.dump(result, entry)

user_agent = {'application_name': 'ThanksLog', 
              'version': '0.0.2alpha',
              'url': 'https://github.com/valepert/thankslog'}

project = 'it'
api = 'w/api.php'
url = 'http://%s.wikipedia.org/%s' %  (project, api)
thanksdir = 'thanks_%s' % project

wiki = simplemediawiki.MediaWiki(url)
simplemediawiki.build_user_agent(**user_agent)

#lastcontinue = u''
query = {'action': 'query', 'list': 'logevents', 'letype': 'thanks',
         'continue': u''} # u'-||' } #, 'lecontinue': lastcontinue}

out = wiki.call(query)
results = out['query']['logevents']
dump_results(results, thanksdir)

