# https://www.hackerrank.com/challenges/html-parser-part-1/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re
from re import finditer


# def parse_starttag(self, shtml):
#     for i in range(len(shtml)):
#         if shtml[i] == '<':
#             self.curr_tag_open = True
#             self.curr_tag_name = True
#             j = i
#             curr_tag = ''
#             curr_attrs = []
#             while j < len(shtml):
#                 if shtml[j] == '/':
#                     if j + 1 >= len(shtml):
#                         raise ValueError("INVALID HTML!!!")
#                     elif shtml[j+1] == '>':
#                         self.handle_startendtag(curr_tag, curr_attrs)
#                 # check end tag
#                 elif shtml[j] == '>':
#                     self.handle_starttag()
#                     self.curr_tag_open = False
#                 # creating current tag
#                 elif str(shtml[j]).isspace() is False and self.curr_tag_name is True:
#                     curr_tag += str(shtml[j])
#                 # curr tag finished; save to stack
#                 elif str(shtml[j]).isspace() is True and self.curr_tag_name is True:
#                     self.tag_stack.append(curr_tag)
#                     self.curr_tag_name = False
#                 # get tag attr if any
#                 elif str(shtml[j]).isspace() is False and self.curr_tag_name is False:
#                 j = j + 1


# create a subclass and override the handler methods
def get_attrs(s_attrs):
    tag_attr = []
    l_attrs = s_attrs.split()

    for i, attr in enumerate(l_attrs):
        # tag name = first attr
        if i == 0:
            continue
        # no attr value
        if attr.split('=') is None:
            tag_attr.append([attr, None])
            continue
        # add attr value
        tag_attr.append([attr.split('=')[0], attr.split('=')[1]])

    return tag_attr


class MyHTMLParser:
    tag_stack = []
    is_comment = False

    def __init__(self):
        self.tag_stack = []
        self.is_comment = False

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("-> {} > {}".format(attr.index(0), attr.index(1)))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("-> {} > {}".format(attr.index(0), attr.index(1)))

    def feed(self, shtml):
        # valid html assumed
        while shtml:
            done_tag = False

            if self.is_comment:
                shtml = None
                continue

            # comment from beginning only
            if '<!--' in shtml:
                self.is_comment = True

            if '-->' in shtml:
                self.is_comment = False

            # closed tag; remove last />
            # no tags in between
            for closed_tag in finditer('<(.*?)/>|$', shtml):
                if closed_tag.start() == closed_tag.end():
                    continue
                tag = shtml[closed_tag.start():closed_tag.end()].split()
                tag = ''.join(item[1:len(item)-1] for item in tag)
                attrs = shtml[closed_tag.start():closed_tag.end()].split()
                s_attrs = []
                if len(attrs) == 1:
                    attrs = []
                else:
                    attrs = attrs[1:]
                    s_attrs = ''.join([str(attr) + ' ' for attr in attrs])
                self.handle_startendtag(tag, get_attrs(s_attrs))

                # do one tag at a time
                done_tag = True

                # move after tag
                if closed_tag.end() != len(shtml)-1:
                    shtml = shtml[closed_tag.end():]
                    break
                shtml = None
                break

            if done_tag is True:
                continue

            # start tag
            # https://www.regular-expressions.info/examples.html#:~:text=Grabbing%20HTML%20Tags&text=matches%20the%20opening,a%20greedy%20star%20would%20do.

            for start_tag in finditer('<([a-z]+) *[^/]*?>|$', shtml):
                # print(start_tag.start(), start_tag.end())
                if start_tag.start() == start_tag.end():
                    continue
                tag = shtml[start_tag.start():start_tag.end()].split()
                tag = ''.join(item[1:len(item)-1] for item in tag)
                attrs = shtml[start_tag.start():start_tag.end()].split()
                s_attrs = []
                if len(attrs) == 1:
                    attrs = []
                else:
                    attrs = attrs[1:]
                    s_attrs = ''.join([str(attr) + ' ' for attr in attrs])
                self.handle_starttag(tag, s_attrs)

                # do one tag at a time
                done_tag = True

                # move after tag
                if start_tag.end() != len(shtml)-1:
                    shtml = shtml[start_tag.end():]
                    break
                shtml = None
                break

            if done_tag is True:
                continue

            # end tag
            for end_tag in finditer('<([a-z]+) */*?>|$', shtml):
                # print(start_tag.start(), start_tag.end())
                if end_tag.start() == end_tag.end():
                    continue
                tag = shtml[end_tag.start():end_tag.end()].split()
                tag = ''.join(item[1:len(item)-1] for item in tag)
                attrs = shtml[end_tag.start():end_tag.end()].split()
                s_attrs = []
                if len(attrs) == 1:
                    attrs = []
                else:
                    attrs = attrs[1:]
                    s_attrs = ''.join([str(attr) + ' ' for attr in attrs])
                self.handle_endtag(tag)

                # move after tag
                if end_tag.end() != len(shtml)-1:
                    shtml = shtml[end_tag.end():]
                    break
                shtml = None
                break


def run_test():
    parser = MyHTMLParser()
    test_html = ["<html><head><title>HTML Parser - I</title></head>", "<body><h1>HackerRank</h1><br /></body></html>"]
    for html in test_html:
        parser.feed(html)


if __name__ == '__main__':
    run_test()
    n = int(input())
    parser = MyHTMLParser()
    for i in range(n):
        parser.feed(input())
