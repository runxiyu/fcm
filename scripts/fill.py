#!/usr/bin/env python3
"""
fill.py - fill data to templates

Originally designed for use in generating https://fcm.andrewyu.org,
expands {{name}} in templates to the value defined in data under
-name-.

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

from sys import argv, stderr
import re

def error(text):
    print(text, file=stderr)

if len(argv) < 3:
    error(f"usage: {argv[0]} data template")
    exit(1)

data_filename = argv[1]
with open(data_filename, 'r') as data_file:
    data_text = data_file.read()
    template_filename = argv[2]
    with open(template_filename, 'r') as template_file:
        while (template_line := template_file.readline()) != '':  # until EOF
            search_result = re.search("{{.*}}", template_line)  # insertion point
            if search_result is None:
                print(template_line, end="")
                continue
            search_result_span = search_result.span()
            variable_placer = template_line[search_result_span[0]:search_result_span[1]]
            variable_name = variable_placer[2:-2]
            variable_name_length = len(variable_name)
            variable_result = re.search(r"\\begin variable_name.*\\end variable_name".replace("variable_name", variable_name), data_text, flags=re.S)
            variable_result_span = variable_result.span()
            variable_data = data_text[variable_result_span[0]:variable_result_span[1]][8+variable_name_length:-6-variable_name_length]  # 8 and 6 are legnth of "\\begin \n" and "\\end \n"
            print(template_line.replace(variable_placer, variable_data), end="")
