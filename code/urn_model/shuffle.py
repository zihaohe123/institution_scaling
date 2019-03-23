#########################################################################
# pre-requisite functions:
import numpy as np
import math


def randomize_globally(sequence):
    # randomize the entire sequence
    return np.random.shuffle(sequence)


def randomize_locally(sequence, institute):
    # randomize locally
    # 1: find first occurrence of institute
    first_pos = sequence.index(institute)
    if first_pos == len(sequence) - 1:
        return sequence
    else:
        # 2: add reshuffled sequence from when institute first appears
        reshuffled = np.random.shuffle(sequence[first_pos + 1:])
        return sequence[:first_pos + 1] + reshuffled


def record_entropy(sequence, institute):
    # record the distribution for 1 institute
    event_pos = np.argwhere(np.array(sequence) == institute).ravel()
    k = len(event_pos)
    total_events = len(sequence) - min(event_pos)
    if k == 1:
        return 0
    bins = range(min(event_pos), len(sequence), k)
    events_per_bin = np.histogram(event_pos, bins)
    # probability = events_per_bin / k
    probability = [each / k for each in events_per_bin]
    print(probability)
    entropy = np.sum([each * math.log(each) for each in probability])
    norm_entropy = entropy / math.log(k)
    return [k, norm_entropy]


def inter_event_times(sequence, institute):
    # find the distribution for 1 institute
    event_pos = np.argwhere(np.array(sequence) == institute).ravel()
    interevent_times = event_pos[1:] - event_pos[:-1]
    return interevent_times


#########################################################################

# functions that output the final product
def record_mean_entropy(sequence):
    # unique institutes
    unique_institutes = set(sequence)
    entropy_institute = np.array([record_entropy(sequence, institute) for institute in unique_institutes])
    max_k = np.max(entropy_institute[:, 1])
    bin_array = [10 ** x for x in np.arange(0, np.log10(max_k), 0.2)]
    bin_vals = [bin_array[i:i + 1] for i in range(0, len(bin_array), 2)]
    mean_entropy_k = [np.mean(np.argwhere(b1 < entropy_institute[:, 1] <= b2).ravel()) for b1, b2 in bin_vals]
    entropy_data = {'entropy_k': mean_entropy_k, 'bins': bin_array}
    return entropy_data


def inter_event_time_dist(sequence):
    # unique institutes
    unique_institutes = set(sequence)
    # find the pos
    events = np.flatten([inter_event_times(sequence, institute) for institute in unique_institutes])
    bin_array = [10 ** x for x in np.arange(0, np.log10(len(events)), 0.2)]
    hist = np.histogram(events, bin_array)
    EventHist = {'histogram': list(hist[0]), 'bins': list(hist[1])}
    return EventHist
