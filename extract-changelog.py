#!/usr/bin/env python3
import html.parser
import re
import sys
import textwrap
from typing import NamedTuple

class AresVersion(NamedTuple):
    major: int
    minor: int = 0

    __recogniser = re.compile(r"(ares_)?v(\d+)([.r](\d+))?")

    def __str__(self) -> str:
        if self.minor != 0:
            return f"ares_v{self.major}r{self.minor:02}"
        else:
            return f"ares_v{self.major}"

    @classmethod
    def from_string(cls, string: str):
        match = cls.__recogniser.search(string)
        if match is None:
            raise ValueError(f"Cannot find ares version in {string!r}")

        major = int(match.group(2))
        minor = int(match.group(4)) if match.group(4) else 0

        return cls(major, minor)


def log(text):
    print(text, file=sys.stderr)


def extract_changelog_block(version, handle):
    res = []
    found_it = False
    for line in handle:
        if line.startswith("</main>"):
            # We hit the end of the changelogs in this file
            if found_it:
                # We got what we wanted.
                break
            else:
                # 404 not found
                raise LookupError(f"No changelog for {version} found")

        if found_it and line.startswith("<h2 id="):
            # We've hit the end of the changelog we wanted.
            break

        if found_it:
            res.append(line)

        elif line.startswith("<h2 id=") and AresVersion.from_string(line) == version:
            found_it = True

    return ''.join(res)


def render_changelog(markup):
    class LayerOuter(html.parser.HTMLParser):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.buffers = [""]

        def close(self):
            super().close()

        def handle_starttag(self, tag, attrs):
            if tag != "br":
                self.buffers.append("")

        def handle_endtag(self, tag):
            content = self.buffers.pop()

            if tag == "p":
                self.handle_data(textwrap.fill(content, width=72) + "\n\n")
            elif tag == "li":
                self.handle_data(
                    textwrap.fill(
                        content,
                        width=72,
                        initial_indent="  - ",
                        subsequent_indent="    ",
                    ) + "\n",
                )
            elif tag == "ul":
                self.handle_data(content + "\n")
            elif tag == "em":
                self.handle_data(f"*{content}*")
            elif tag == "strong":
                self.handle_data(f"**{content}**")
            else:
                log(f"Ignoring tag {tag}")

        def handle_data(self, data):
            if not data.isspace():
                self.buffers[-1] += data

        def result(self):
            return self.buffers[0]

    layerouter = LayerOuter()
    layerouter.feed(markup)
    layerouter.close()

    return layerouter.result()


def main(args):
    [_, raw_version, source] = args

    version = AresVersion.from_string(raw_version)

    with open(source, "r") as handle:
        block = extract_changelog_block(version, handle)

    print(render_changelog(block), end='')

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
