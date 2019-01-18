# from django.test import TestCase

# Create your tests here.

import os


a = [1,2,3]
try:
    for i in range(4):
        a[i]
except Exception as e:
    print(repr(e))
    print(os.path.basename(__file__))
