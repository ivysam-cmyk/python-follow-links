# Following links in python
Get the href value from <a> tags at the particular position
Follow that link
Repeat this the stated number of times

The starting code for urllib and BeautifulSoop is copied

```python
 import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# change the below
tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) 
```
Solution:
1.Cycle through the <a> tags 
2.Once you get to the 18th position
3.Record the link(href value)
4.Go to that link and repeat steps 1-4 another 6 times