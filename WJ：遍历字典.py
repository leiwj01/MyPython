#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = {'a': '1', 'b': '2', 'c': '3'}
for key in a:
    print(key + ':' + a[key])
print('- ' * 10)
for key in a.keys():
    print(key + ':' + a[key])
print('- ' * 10)
for value in a.values():
    print(value)
print('- ' * 10)
for key, value in a.items():
    print(key, value)
print('- ' * 10)
for test in a.items():
    print(test)
