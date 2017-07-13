# Create by Fedor Tsyganov on July 13th 2017

from range import *

test1 = RangeUtil()
test1.add_range(Range(3, 3))
test1.add_range(Range(4, 5))
test1.add_range(Range(2, 4))

test2 = RangeUtil()
test2.add_range(Range(94133, 94133))
test2.add_range(Range(94200, 94299))
test2.add_range(Range(94226, 94399))

print test1
print test2