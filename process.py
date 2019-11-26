#!/usr/bin/python
# coding=utf-8

import re

CHAPTER_RE = re.compile(r"### Chapter (?P<num>\d+):")
OTHER_HEADING = re.compile(r"#{2,} (?P<heading>\w+)")

anchor_with_link = " <a href='#{0}' name='{0}'>🔗</a>"

with open("README.md") as f:
    lines = f.read()

lines = lines.splitlines()

output = []

for line in lines:
    if "<a" not in line:
        chap_match = CHAPTER_RE.match(line)
        if chap_match:
            line += anchor_with_link.format("chapter-" + chap_match.group("num"))
        else:
            head_match = OTHER_HEADING.match(line)
            if head_match:
                line += anchor_with_link.format(head_match.group("heading").lower())

    if not line.endswith("  "):
        line += "  "

    output.append(line)

with open("README.md", "w") as f:
    f.write("\n".join(output))
