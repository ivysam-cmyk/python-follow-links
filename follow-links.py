import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Use link as string
# First name is in the link
url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
# Initial position is 1
position = 1
# the number of times a link is visited
link_visited = 0
for tag in tags:
  link = tag.get('href', None)
  if (position == 3):
    name = tag.contents[0] 
    print(name)
    link_visited += 1
    if (link_visited == 4):
      # At the 4th time that the link is clicked record the name and break
      name = tag.contents[0] 
      print(name)
      break
    url = link
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # reset the position so that it can be used again after opening the url
    position = 1

  position += 1