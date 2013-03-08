#!/usr/bin/python

__author__ = 'David Reiss <davidn@gmail.com>'

import unittest

import tier

class TierTest(unittest.TestCase):
  def testUnpackBits(self):
    out = tier.UnpackBits(0b00011011, 4)
    self.assertEqual('OLFN', out)


if __name__ == '__main__':
  unittest.main()
