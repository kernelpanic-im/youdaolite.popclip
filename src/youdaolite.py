#!/usr/bin/python

import urllib
import os
import urllib2
import json


__API_KEY_NAME__ = 'kernelpanic'
__API_KEY_VALUE__ = '482091942'


def query_youdao(word):
    parameters = {
        'keyfrom': __API_KEY_NAME__,
        'key': __API_KEY_VALUE__,
        'type': 'data',
        'doctype': 'json',
        'version': '1.1',
        'q': word}

    query_string = urllib.urlencode(parameters)
    query_url = "http://fanyi.youdao.com/openapi.do?{0}".format(query_string)
    request = urllib2.urlopen(query_url)
    json_response = json.loads(''.join(request.readlines()))
    #print json_response
    try:
        if('basic' in json_response):
            result = u'\n'.join(json_response['basic']['explains'])
            return result
        elif('web' in json_response):
            #print 'web'
            web_results = json_response['web']
            results = []
            for result in web_results:
                results.append(u'{0}:{1}'.format(result['key'], u' '.join(result['value'])))
            return u'\n'.join(results)

        elif('translation' in json_response):
            #print 'translation'
            result = u'\n'.join(json_response['translation'])
            return result
    except Exception, e:
        print(e)
        return None


popclip_text = os.getenv('POPCLIP_TEXT')
display_text = query_youdao(popclip_text)
print(display_text.encode('utf-8'))
