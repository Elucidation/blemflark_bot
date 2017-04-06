# -*- coding: utf-8 -*-
import re
import time
import locale
from datetime import datetime
from math import isinf

# For converting from string numbers with english-based commas to floats
#locale.setlocale(locale.LC_ALL, 'eng_USA') # Windows
locale.setlocale(locale.LC_ALL, 'en_GB.utf8') # Linux

def getResponseFooter():
  return "\n\n---\n\n[^(1 Blemflark = $0 USD)](https://www.reddit.com/r/rickandmorty/comments/62ygal/the_value_of_the_blemflark/)^( | price not guaranteed |) [^(`what is my purpose`)](https://github.com/Elucidation/blemflark_bot 'I'll tell you, for money.')"

def getValue(value_str):
  # Strings with more than 9000 characters are considered too big to handle so
  # we don't run into char limits when generating a reply
  if (len(value_str)) > 9000:
    value = locale.atof('inf')
  else:
    value = locale.atof(value_str)
  return value

def getCommentDepth(comment):
  depth = 0
  while not comment.is_root:
    comment = comment.parent()
    depth += 1
  return depth

def generateResponseMessage(search_result):
  match = search_result.groups()[1] # Middle group
  value_str = match.split()[0]
  
  if len(match) > 1000 or len(value_str) > 300:
    # message or value was too big, generate a different message
    msg = u"# **Nope.** I'm just going to say it is $0 USD.\n"
  else:
    value = getValue(value_str) # pass found value string
    quote = u"> ... {}{}{} ...".format(search_result.groups()[0], match, search_result.groups()[2])
    if value > 1e15:
      msg = u"{}\n\n* {:,g} Blemflarks → **$0 USD**\n".format(
        quote, value)
    elif value.is_integer():
      msg = u"{}\n\n* {:,d} Blemflarks → **$0 USD**\n".format(
        quote, int(value))
    else:
      msg = u"{}\n\n* {:,.8g} Blemflarks → **$0 USD**\n".format(
      quote, value)

  return u"{}{}".format(msg, getResponseFooter())


# Look for '<number> blemflark' ignore case (blemflarks accepted implicitly)
# Also handles common mispellings of blemflark
# Works for positive negative floats, but fails softly on EXP
# Also catches neighboring region around it
# Ignore numbers > 300 chars on either side of decimal
# Also requires a question-like statement
p = re.compile('([^\n\.\,\r\d-]{0,30})(-?[\d|,]{0,300}\.{0,1}\d{1,300} bl?emfl?arc?k[\w]{0,80})([^\n\.\,\r\d-]{0,30})', re.IGNORECASE)
def searchForBlemflarks(body_text):
  if any([x in body_text.lower() for x in ['?', 'how much', 'what is']]):
    return p.search(body_text)
  return None


# Check if comment has a comment by this bot already, or is a comment by bot
def previouslyRepliedTo(comment, me):
  if comment.author == me:
    return True
  comment.refresh() # So we can see replies
  for reply in comment.replies.list():
    if reply.author == me:
      return True
  return False


def waitWithComments(sleep_time, segment=60):
  """Sleep for sleep_time seconds, printing to stdout every segment of time"""
  print("\t%s - %s seconds to go..." % (datetime.now(), sleep_time))
  while sleep_time > segment:
    time.sleep(segment) # sleep in increments of 1 minute
    sleep_time -= segment
    print("\t%s - %s seconds to go..." % (datetime.now(), sleep_time))
  time.sleep(sleep_time)

def logMessage(comment, status=""):
  print("{} | {} {}: {}".format(datetime.now(), comment.id, status, comment.body[:80].replace('\n','\\n').encode('utf-8')))
