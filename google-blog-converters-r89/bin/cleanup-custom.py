#!/usr/bin/python

import sys

wp_file = open(sys.argv[1])
for wp_line in wp_file:
    wp_line = wp_line.strip()
    #if wp_line.startswith('<?xml version="1.0" encoding="UTF-8'):
    #    wp_line = '<?xml version="1.0" encoding="iso-8859-1"?>'
    wp_line = wp_line.decode('iso-8859-1').encode('utf-8')
    if wp_line.startswith('<title>'):
        wp_line = wp_line.replace('<title>', '<title><![CDATA[')
    if wp_line.endswith('</title>'):
        wp_line = wp_line.replace('</title>', ']]></title>')
    if wp_line.startswith('<wp:post_name>'):
        wp_line = wp_line.replace('<wp:post_name>', '<wp:post_name><![CDATA[')
    if wp_line.endswith('</wp:post_name>'):
        wp_line = wp_line.replace('</wp:post_name>', ']]></wp:post_name>')
    if wp_line.startswith('<content:encoded>'):
        wp_line = '<content:encoded><![CDATA['
    if wp_line.endswith('</content:encoded>'):
        wp_line = wp_line.replace('</content:encoded>', ']]></content:encoded>')
    print wp_line

wp_file.close()
