import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Use link as string
# First name is in the link
url = "http://py4e-data.dr-chuck.net/known_by_Eassan.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# the loop restarts when another link is visited
boolean = True
link_visited = 0
# stop visiting more links upon reaching the 7th person

redirect_limit = int(input("Enter count: "))
tag_limit = int(input("Enter position: "))

while boolean == True:
# Initial position is 1
  tag_position = 1
  tags = soup('a')
# the number of times a link is visited
  for tag in tags:
    link = tag.get('href', None)
    if (tag_position == tag_limit):
      name = tag.contents[0] 
      print(name)
      link_visited += 1
      if (link_visited == redirect_limit):
        boolean = False
        # if the above doesn't stop the loop, then...
        break
      url = link
      html = urllib.request.urlopen(url, context=ctx).read()
      soup = BeautifulSoup(html, 'html.parser')
      # need to change the tags variable, include it in a loop
      tags = soup('a')
      # tags does change but the tags used in 'for' loop does not change
      # reset the tag_position so that it can be used again after opening the url

    tag_position += 1
