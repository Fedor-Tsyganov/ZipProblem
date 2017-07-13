# Create by Fedor Tsyganov on July 13th 2017

# Range Model
class Range:
    def __init__(self, low, upper):
        if low <= upper:
            self.low = low
            self.upper = upper
        else:
            self.low = upper
            self.upper = low

    def __str__(self):
        return '[%d,%d]' % (self.low, self.upper)

    def update_low(self, new_low):
        self.low = new_low

    def update_upper(self, new_upper):
        self.upper = new_upper

# Range Util Controller
class RangeUtil:

    def __init__(self):
        self.list_of_ranges = list()

    def add_range(self, range_to_add):
        if len(self.list_of_ranges) == 0:
            self.list_of_ranges.append(range_to_add)
        else:
            canAdd = False
            objToRemove = []
            for r in self.list_of_ranges:
                # Update Upper Bound
                if range_to_add.low not in xrange(r.low, r.upper+1) and range_to_add.upper in xrange(r.low, r.upper+1):
                    range_to_add.update_upper(r.upper)
                    objToRemove.append(r)
                    canAdd = True
                # Update Lower Bound
                elif range_to_add.low in xrange(r.low, r.upper+1) and range_to_add.upper not in xrange(r.low, r.upper+1):
                    range_to_add.update_low(r.low)
                    objToRemove.append(r)
                    canAdd = True
                # Update both Lower and Upper bounds
                elif r.low in xrange(range_to_add.low, range_to_add.upper+1) and r.upper in xrange(range_to_add.low, range_to_add.upper+1):
                    r.update_upper(range_to_add.upper)
                    r.update_low(range_to_add.low)
                    objToRemove.append(r)
                # Update both Lower and Upper bounds
                elif range_to_add.low in xrange(r.low, r.upper+1) and range_to_add.upper in xrange(r.low, r.upper+1):
                    range_to_add.update_upper(r.upper)
                    range_to_add.update_low(r.low)
                    objToRemove.append(r)
                # Range is out of bounds, add it
                else:
                    canAdd = True

            if canAdd:
                for o in objToRemove:
                    self.list_of_ranges.remove(o)

                self.list_of_ranges.append(range_to_add)

    def __str__(self):
        return ' '.join(map(str, self.list_of_ranges))
