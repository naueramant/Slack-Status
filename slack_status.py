#! /usr/bin/env python3

from urllib import request, parse
import json, os, subprocess, re
from time import time
from functools import lru_cache

config_path = '~/.config/slack-status.json'

default_values = {
  'rules': {
    'status_emoji': '',
    'status_duration': 3600 # an hour
  }
}

def update_status():
    config = get_config()

    text, emoji, duration = check_rules()
    expires = int(time()) + duration

    if text:
      params = {
            'token': config['token'],
            'profile': {
              'status_text': text, 
              'status_emoji': emoji,
              'status_expiration': expires
          }
      }

      query = parse.urlencode(params)     

      req =  request.Request(f'https://slack.com/api/users.profile.set?{query}')
      resp = request.urlopen(req)

      resp_json = json.loads(resp.read().decode('utf-8'))

      if resp_json['ok']:
        print('updated status:', text, emoji, 'expires', expires)
      else:
        print('Failed to update status')
        print(resp_json)

def get_essid():
  return subprocess.check_output(['iwgetid', '-r']).decode('utf-8').strip()

@lru_cache()
def get_config():
  path = os.path.expanduser(config_path)

  try:
    with open(path, 'rb') as f:
      config = json.loads(f.read())
      check_if_valid_config(config)
      return config

  except FileNotFoundError:
    print('Failed to load config file!')
    exit(-1)

def check_if_valid_config(config):
  if 'token' not in config:
    print('Missing authentication token in config')
    exit(-1)

  if 'rules' in config:
    for i, rule in enumerate(config['rules']):
      if 'essid_regex' not in rule:
        print(f'essid_regex missing in rule {i + 1}')
        exit(-1)
      if 'status_text' not in rule:
        print(f'status_text missing in rule {i + 1}')
        exit(-1)

def check_rules():
  text = None
  emoji = default_values['rules']['status_emoji']
  duration = default_values['rules']['status_duration']

  essid = get_essid()
  config = get_config()
  
  for rule in config['rules']:
    pattern = re.compile(rule['essid_regex'])
    
    if pattern.match(essid):
      text = rule['status_text']

      if 'status_emoji' in rule:
        emoji = rule['status_emoji']

      if 'status_duration' in rule:
        duration = rule['status_duration']

      break

  return text, emoji, duration

if __name__ == "__main__":
    update_status()