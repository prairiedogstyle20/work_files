#!/usr/bin/env python

exim_log_file = "exim_test"

def main():
    f = open(exim_log_file, 'r')
    content = f.read()
    print (content)

main()
