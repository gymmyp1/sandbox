#Implementation of ordered COO for comparison to hacoo
import bisect

class coo_t:
    def __init__(self, modes=None):
        #just a list of tuples
        self.indexes = []
        self.n_indexes = 0

    def set(self, idx):
        bisect.insort(self.indexes,idx)
        return list


def read(file):
	with open(file, 'r') as reader:
		# Create the tensor
		tns = coo_t()

		for row in reader:
			row = row.split()
			# Get the value
			val = float(row.pop()) #we're not using val for now
			# The rest of the line is the indexes
			idx = [int(i) for i in row]

			tns.set(idx)

	reader.close()
	return tns
