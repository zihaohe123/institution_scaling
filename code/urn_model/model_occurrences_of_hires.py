# assume there is data of the form:
# sequence = [1,2,6,3,7,...]
# each number corresponds to a unique institute ID
import sys
sys.path.append('..')
import numpy as np
import pandas as pd
import shutil, os, time
import pickle as pk
from utils.pkl_io import open_pkl_file
from utils.directories import *


def unique_colors(sequence, n):
    return set(sequence[:n])


def total_num_researchers(sequence):
    return len(sequence)


def total_num_institutes(sequence):
    return len(unique_colors(sequence, len(sequence)))


def record_entropy(sequence, institute):
    event_pos = np.argwhere(np.array(sequence) == institute).ravel()
    k = len(event_pos)
    if k == 1:
        return [1, 0]

    total_events = len(sequence) - min(event_pos)

    bin_width = int(round(total_events / k))

    bins = range(min(event_pos), len(sequence), bin_width)
    events_per_bin = np.histogram(event_pos, bins)[0]
    probability = events_per_bin / k
    probability = probability[probability > 0]
    entropy = -np.sum(probability * np.log(probability))
    norm_entropy = entropy / np.log(k)

    return [k, norm_entropy]


def record_mean_entropy(sequence):
    # unique institutes
    unique_institutes = set(sequence)
    # print(len(unique_institutes))
    entropy_institute = []
    num = 0
    for institute in unique_institutes:
        num += 1
        if num % 100 == 0:
            print('entropy, the {}th institution'.format(num), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        k, norm_entropy = record_entropy(sequence, institute)
        # print([k,norm_entropy])
        if norm_entropy is not None:
            entropy_institute.append([k, norm_entropy])
    entropy_institute = np.array(entropy_institute)

    # print(entropy_institute)
    max_k = np.max(entropy_institute[:, 0])
    delta_k = 0.05
    bin_array = [10 ** x for x in np.arange(0, np.log10(max_k) + delta_k, delta_k)]
    bin_vals = np.array([bin_array[i:i + 2] for i in range(0, len(bin_array), 1) if len(bin_array[i:i + 2]) > 1])
    # print(bin_vals)
    mean_entropy_k = []
    for b1, b2 in bin_vals:
        binned_entropy = entropy_institute[b1 < entropy_institute[:, 0]]
        binned_entropy = binned_entropy[binned_entropy[:, 0] <= b2]
        if len(binned_entropy) > 0:
            mean_entropy = np.mean(binned_entropy[:, 1])
        else:
            mean_entropy = np.nan
        mean_entropy_k.append(mean_entropy)
    # mean_entropy_k = [np.mean(np.argwhere(b1<entropy_institute[:,1]<=b2).ravel()) for b1,b2 in bin_vals]
    # print(mean_entropy_k)
    entropy_data = {'entropy_k': mean_entropy_k, 'bin_low': list(bin_vals[:, 0]), 'bin_high': list(bin_vals[:, 1])}
    return entropy_data


def record_local_mean_entropy(entropy_institute):
    entropy_institute = np.array(entropy_institute)
    max_k = np.max(entropy_institute[:, 0])
    delta_k = 0.05
    bin_array = [10 ** x for x in np.arange(0, np.log10(max_k) + delta_k, delta_k)]
    bin_vals = np.array([bin_array[i:i + 2] for i in range(0, len(bin_array), 1) if len(bin_array[i:i + 2]) > 1])
    # print(bin_vals)
    mean_entropy_k = []
    for b1, b2 in bin_vals:
        binned_entropy = entropy_institute[b1 < entropy_institute[:, 0]]
        binned_entropy = binned_entropy[binned_entropy[:, 0] <= b2]
        # print(binned_entropy)
        if len(binned_entropy) > 0:
            mean_entropy = np.mean(binned_entropy[:, 1])
        else:
            mean_entropy = np.nan
        mean_entropy_k.append(mean_entropy)
    entropy_data = {'entropy_k': mean_entropy_k, 'bin_low': list(bin_vals[:, 0]), 'bin_high': list(bin_vals[:, 1])}
    return entropy_data


def inter_event_times(sequence, institute):
    # find the distribution for 1 institute
    event_pos = np.argwhere(np.array(sequence) == institute).ravel()
    interevent_times = event_pos[1:] - event_pos[:-1]
    return interevent_times


def flatten(lol):
    return [s for l in lol for s in l]


def inter_event_time_dist(sequence):
    # unique institutes
    unique_institutes = set(sequence)
    # find the pos
    events = [inter_event_times(sequence, institute) for institute in unique_institutes]
    events = flatten(events)
    delta_t = 0.05
    bin_array = [10 ** x for x in np.arange(0, np.log10(max(events)) + delta_t, delta_t)]
    bin_vals = np.array([bin_array[i:i + 2] for i in range(0, len(bin_array), 1) if len(bin_array[i:i + 2]) > 1])
    hist = np.histogram(events, bin_array)
    EventHist = {'histogram': list(hist[0]), 'bin_low': list(bin_vals[:, 0]), 'bin_high': list(bin_vals[:, 1])}
    return EventHist


def local_inter_event_time_dist(events):
    # print(events)
    events = np.array(events)
    delta_t = 0.05
    bin_array = [10 ** x for x in np.arange(0, np.log10(len(events)), delta_t)]
    bin_vals = np.array([bin_array[i:i + 2] for i in range(0, len(bin_array), 1) if len(bin_array[i:i + 2]) > 1])
    # print(bin_array)
    hist = np.histogram(events, bin_array)
    EventHist = {'histogram': list(hist[0]), 'bin_low': list(bin_vals[:, 0]), 'bin_high': list(bin_vals[:, 1])}
    return EventHist


def randomize_globally(sequence):
    rand_seq = sequence[:]
    np.random.shuffle(rand_seq)
    return rand_seq


def randomize_locally(sequence, institute):
    # find first occurence of institute
    first_pos = sequence.index(institute)
    if first_pos == len(sequence) - 1:
        return sequence
    else:
        reshuffled = sequence[first_pos + 1:]
        np.random.shuffle(reshuffled)
        return sequence[:first_pos + 1] + reshuffled


def record_growth_statistics(sequence):
    # record:
    #       - Zipf's law: log-binned research size distribution
    #       - Heap's law: {# researchers, # institutions}
    #       - sequence entropy(k)
    #       - times between researchers join institutes

    # Zipf's law
    print("Zipf's law", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    delta_n = 0.05
    bin_array = [10 ** x for x in np.arange(0, np.log10(len(sequence)) + delta_n, delta_n)]
    bin_vals = np.array([bin_array[i:i + 2] for i in range(0, len(bin_array), 1) if len(bin_array[i:i + 2]) > 1])
    num_res_per_institute = [sequence.count(institute) for institute in set(sequence)]
    hist = np.histogram(num_res_per_institute, bin_array)

    # hist[0]= hist[0]
    ZipfLaw = {'histogram': list(hist[0]), 'bin_low': list(bin_vals[:, 0]), 'bin_high': list(bin_vals[:, 1])}

    # Heap's law: {# researchers,#institutes}
    print("Heap's law", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    HeapsLaw = {'num_researchers': list(range(len(sequence))),
                'num_institutes': [len(set(sequence[:n])) for n in range(len(sequence))]}

    # entropy
    print("entropy", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    EntropyK = record_mean_entropy(sequence)

    # inter-event times
    print('inter-event times', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    InterEventTimes = inter_event_time_dist(sequence)
    data = {'ZipfLaw': ZipfLaw, 'HeapsLaw': HeapsLaw, 'EntropyK': EntropyK, 'InterEventTimes': InterEventTimes}
    return data


def local_growth_statistics(growth_data, sequence):
    local_null_growth_data = {'ZipfLaw': growth_data['ZipfLaw'], 'HeapsLaw': growth_data['HeapsLaw'], 'EntropyK': [],
                              'InterEventTimes': []}
    events = []
    entropy_institute = []
    for institute in set(sequence):  # range(total_num_institutes(sequence)):
        null_local_data = randomize_locally(sequence, institute)
        # compute entropy for institute
        e_i = record_entropy(null_local_data, institute)
        e_i = list(e_i)
        entropy_institute.append(e_i)
        # compute inter-event times
        inter_events = inter_event_times(null_local_data, institute)
        inter_events = list(inter_events)
        events.append(inter_events)
    events = flatten(events)

    local_null_growth_data['EntropyK'] = record_local_mean_entropy(entropy_institute)
    local_null_growth_data['InterEventTimes'] = local_inter_event_time_dist(events)
    return local_null_growth_data


def finish_data_collection(sequence):
    null_global_data = randomize_globally(sequence)

    print("real data analysis started", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    growth_data = record_growth_statistics(sequence)
    print("real data analyzed", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    print("global random data analysis started", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    global_null_growth_data = record_growth_statistics(null_global_data)
    print("global random data analyzed", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    print("local random data analysis started", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    local_null_growth_data = local_growth_statistics(growth_data, sequence)
    print("local random data analyzed", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    growth_data = {'original': growth_data, 'local_null': local_null_growth_data, 'global_null': global_null_growth_data}
    return growth_data


def export_growth_data(growth_data):
    for data in growth_data.keys():
        add_folder(data)
        for data_type in ['ZipfLaw', 'HeapsLaw', 'EntropyK', 'InterEventTimes']:
            export_data = growth_data[data][data_type]
            df = pd.DataFrame(data=export_data)
            # export to folder "growth_data/", "local_null/", or "global_null/"
            path = os.path.join(directory_urn_model, data, data_type+".csv")
            df.to_csv(path, index=False)


def add_folder(folder):
    path = os.path.join(directory_urn_model, folder)
    # delete old folder and contents
    if os.path.exists(path):
        shutil.rmtree(path)
    # if not os.path.exists(folder+"/"):
    os.mkdir(path)


def merge_data():
    # put the same kind of result in one csv file
    add_folder(os.path.join(directory_urn_model, 'merged_data'))
    for result_type in ['ZipfLaw', 'HeapsLaw', 'EntropyK', 'InterEventTimes']:
        merged_data = []
        for data_type in ['original', 'local_null', 'global_null']:
            path = os.path.join(directory_urn_model, data_type, result_type+".csv")
            data = pd.read_csv(path)
            columns = data.columns.tolist()
            new_columns = {column: "{}_{}".format(column, data_type) for column in columns}
            data.rename(columns=new_columns, inplace=True)
            merged_data.append(data)
        new_data = pd.concat([each for each in merged_data], axis=1)
        new_data.to_csv(os.path.join(directory_urn_model, 'merged_data', result_type+".csv"), index=False)


def main():
    cleaned_file_name = "CleanedSequenceData2.csv"
    if os.path.isfile(cleaned_file_name):
        noduplicate_df = pd.read_csv(os.path.join(directory_urn_model, cleaned_file_name))
    else:
        authorId_affId_sequence = open_pkl_file(directory_urn_model, 'authorId_affId_sequence')[:10000]
        authorId_affId_sequence = np.asanyarray(authorId_affId_sequence, dtype=int)
        authorId_sequence = authorId_affId_sequence[:, 0]
        affId_sequence = authorId_affId_sequence[:, 1]
        print("loaded...", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        affil_data = {"author_id": authorId_sequence, "affil_id": affId_sequence}
        df = pd.DataFrame(data=affil_data)
        noduplicate_df = df.drop_duplicates()
        noduplicate_df.to_csv(os.path.join(directory_urn_model, cleaned_file_name), index=False)
        print("cleaned", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # sequence of affiliations
    seq = np.array(noduplicate_df[['affil_id']].loc[:].values.tolist())
    seq = seq.flatten().tolist()

    start_time = time.time()
    growth_data = finish_data_collection(seq)
    export_growth_data(growth_data)
    merge_data()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
