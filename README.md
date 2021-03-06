# robotsparsetools
robots.txt is important when crawling website  

This module will help you parse robots.txt

# Install
```bash
$ pip install robotsparsetools
```

# Usage
## Parse
Please create an Parse instance first  

```python
from robotsparsetools import Parse

url = "URL of robots.txt you want to parse"
p = Parse(url) # Create an instance. Returns a Parse class with the useragent as the key

# Get allow list
p.Allow(useragent)

# Get disallow list
p.Disallow(useragent)

# Get value of Crawl-delay(Return value is int or None)
p.delay(useragent)

# Find out if crawls are allowed
p.can_crawl(url, useragent)
```

If no useragent is specified, the value of '*' will be referenced  

Also, since the Parse class inherits from dict, you can also use it like dict

```python
from robotsparsetools import Parse

p = Parse(url)
p["*"]
p.get("*") # Can also use get method
``` 

## Read
You can parse its contents by passing a text or local path to Read

```python
from robotsparsetools import Read
import requests

url = "URL of robots.txt you want to parse"
r = requests.get(url)
p = Read(r.text)

path = "File path of robots.txt you want to parse"
p = Read(path)
```

The return value is a Parse instance

## Make(✨ new in 1.3)
You can easily generate the contents of robots.txt by using this

```python
from robotsparsetools import Make

base = Make()

base.add_sitemap("https://xxxxxx.com/sitemap.xml")
all = base.add_useragent("*")
all.add_disallow("/hoge")

bot = base.add_useragent("bot")
bot.add_allow(["/example", "/any/*"])
bot.add_disallow(["/test", "/xxx/"])

path = "File path"
base.to_file(path) # Output the result to a file

print(base.make()) # Generation
```

Below is the result of this code

```
User-agent: *
Disallow: /hoge

User-agent: bot
Disallow: /test
Disallow: /xxx/
Allow: /example
Allow: /any/*

Sitemap: https://xxxxxx.com/sitemap.xml
```

## Error Classes
Also, there are three error classes

```python
from robotsparsetools import NotURLError, NotFoundError, UserAgentExistsError
```

## Command line
You can use rp command

```bash
$ rp URL # If you do not specify any options, output Y if crawl is allowed, N if not allowed
$ rp -a URL # Output the Allow list
$ rp -d URL # Output the Disallow list
$ rp -c URL # Output the Crawl-delay
```

# License
This program's license is [MIT](https://github.com/mino-38/robotsparsetools/blob/main/LICENSE)

[![Downloads](https://pepy.tech/badge/robotsparsetools)](https://pepy.tech/project/robotsparsetools)
