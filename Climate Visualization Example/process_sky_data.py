import sys
entry = list(sys.argv)[1]

def process_sky_data(entry):
    things = entry.split(' ')
    coverages = [int(coverage.split(':')[1]) for coverage in things[0::2]]
    heights = [int(height) for height in things[1::2]]
    return list(zip(coverages, heights))
print(process_sky_data(entry))