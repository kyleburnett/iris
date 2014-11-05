#
# Name: basket.py
# Description: Useful for putting iris samples into respective
#   baskets by type.
#
# Author(s): Kyle Burnett
#

class Basket(dict):
	def __getitem__(self, idx):
        self.setdefault(idx, [])
        return dict.__getitem__(self, idx)

    # Expects a parsed and correctly typed sample where the first
    # 4 elements of the sample array are floats and the last element
    # denotes the iris type
	def putSample(self, sample):
        # The last segment identifies the iris type
        irisType = sample[-1]
        # Construct list which holds the attributes for sample
        attributes = sample[:-1]
        self[irisType].append(attributes)