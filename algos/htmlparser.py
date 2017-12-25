import re


class Tag:
    def __init__(self, match):
        self.html_text = match.group()
        self.attrs = self._get_attrs()
        self.startAt = match.start()

    @property
    def name(self):
        return re.search(r"<([a-zA-Z0-9]+)\s?", self.html_text).group(1)

    def closing(self):
        closing = "</{}>".format(self.name)
        return closing

    def get(self, x):
        return self.attrs.get(x)

    def _get_attrs(self):
        attrs = {}
        for substr in mysplit(self.html_text[1:-1]):
            if "=" in substr.strip():
                attr, value = substr.split("=")
                attrs[attr] = value.replace('"', " ").strip()
        return attrs

    def __repr__(self):
        return self.html_text

    def meet(self, attrs):
        assert isinstance(attrs, dict)
        for k, v in attrs.items():
            if not v in self.attrs.get(k, ""):
                return False
        return True


def mysplit(text):
    """
    does not split in quotes
    :param text:
    :return:
    """
    in_quote = False
    temp = ""
    for ch in text:
        if ch == " " and not in_quote:
            yield temp
            temp = ""
        elif ch == '"':
            in_quote = not in_quote
        else:
            temp += ch
    yield temp


class PageElement:
    def __init__(self, html_text):
        self.html_text = html_text

    def __repr__(self):
        return self.html_text

    def tag(self, name, attrs=None):
        html_text = self.html_text
        for match in re.finditer(r"<{}\s?.*?>".format(name), html_text):
            tag = Tag(match)
            if attrs and not tag.meet(attrs):
                continue
            return tag
        return None

    def tags(self, name, attrs=None):
        lst = []
        html_text = self.html_text
        for match in re.finditer(r"<{}\s?.*?>".format(name), html_text):
            tag = Tag(match)
            if attrs and not tag.meet(attrs):
                continue
            lst.append(tag)
        return lst

    def text(self):
        return re.sub(r"<.*?>", "", self.html_text)

    def element(self, name, attrs=None):
        html_text = self.html_text
        tag = self.tag(name, attrs=attrs)
        if tag:
            element_start = tag.startAt
            closing_tag = tag.closing()
            element_end = html_text.find(tag.closing(), element_start)
            return PageElement(html_text[element_start:element_end + len(closing_tag)])

    def all_elements(self, name, attrs=None):
        html_text = self.html_text
        elements = []
        for tag in self.tags(name, attrs=attrs):
            element_start = tag.startAt
            closing_tag = tag.closing()
            element_end = html_text.find(tag.closing(), element_start)
            if element_end == -1:
                raise ValueError()
            elements.append(PageElement(html_text[element_start: element_end + len(closing_tag)]))
        return elements
