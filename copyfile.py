#!/usr/bin/env python3

def copy_file(src, dst):
    with open(src, 'r') as src_file:
        with open(dst, 'a') as dst_file:
            for line,value in enumerate(src_file.readlines()):
                result = '{} {}'.format(line+1,value)
                dst_file.write(result)
if __name__ == '__main__':
    copy_file('shiyanlou.txt','shiyanlou_copy.txt')
