#!/usr/bin/env python3

"""

gitlogtorss.py

Originally designed for use in generating https://fcm.andrewyu.org,
translates a git log to an RSS feed.

Python 3.8+ required!

Copyright (C) 2022  Andrew Yu <andrew@andrewyu.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys

head = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>
<title>Free Computing Movement</title>
<link>https://fcm.andrewyu.org/</link>
<description>Liberty in computing, both free software and free hardware.</description>
"""

item = """<item>
    <title>{title}</title>
    <link>{link}</link>
    <!--guid></guid-->
    <pubDate>{date}</pubDate>
    <description>{description}</description>
</item>
"""

tail = """</channel>
</rss>"""


