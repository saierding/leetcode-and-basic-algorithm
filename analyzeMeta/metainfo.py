#!/usr/bin/env python3
import re
import json
import argparse
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(description='this file is a simple'
                                 'facedlog parser.')
parser.add_argument('version',
                    type=str,
                    choices=['02', '05'],
                    help='core version, eg: 02, 05')
parser.add_argument('logfile', type=str, help='facedlog file name')
parser.add_argument('-f',
                    '--first',
                    action='store_true',
                    help='if only cal first alert of a track')
parser.add_argument('-p',
                    '--plot',
                    action='store_true',
                    help='if plot the results')
args = parser.parse_args()
print('args: ', args, '\n')

suffix05 = [
    'decode', 'analyze', 'dispatch', 'search', 'aggregator', 'store', 'pub',
    'total latency'
]

suffix02 = ['decode', 'analyze', 'track-shaper', 'pub', 'pub-start-diff']

max_results_file = args.logfile + '-max'
if args.first:
    max_results_file += '-only-first'
else:
    max_results_file += '-all'


def parse05(file_name):
    res_min = [10000000 for i in range(8)]
    res_max = [0 for i in range(8)]
    res_avg = [0 for i in range(8)]
    count = 0
    cache = {}
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if 'alert' in line and 'meta_info' in line:
                line = normJson(line)
                track_id = re.search(r'track_id":"(.*?)"', line)
                if not track_id or track_id.group(1) in cache:
                    continue
                if args.first:
                    cache[track_id.group(1)] = 1
                match = re.search(r'"meta_info":{.*?}', line)
                if match:
                    match_string = match.group()
                    match = re.search(r'{.*?}', match_string)
                    if match:
                        d = json.loads(s=match.group())
                        if len(d) != 8:
                            continue
                        temp = get_duration_05(d)
                        count += 1
                        for i in range(len(temp)):
                            if temp[i] < res_min[i]:
                                res_min[i] = temp[i]
                            if temp[i] > res_max[i]:
                                res_max[i] = temp[i]
                            res_avg[i] += temp[i]

    for i in range(len(res_avg)):
        if count != 0:
            res_avg[i] /= count

    print_res(res_min, "min", suffix05)
    print_res(res_max, "max", suffix05)
    print_res(res_avg, "avg", suffix05)


def parse02(file_name):
    res_min = [1000000 for i in range(5)]
    res_max = [0 for i in range(5)]
    res_max_info = [0 for i in range(5)]
    res_avg = [0 for i in range(5)]
    count = 0
    miss_fast_3_count = 0
    cache = {}
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if 'alert' in line and 'meta_info' in line:
                line = normJson(line)
                track_id = re.search(r'track_id":"(.*?)"', line)
                if not track_id or track_id.group(1) in cache:
                    continue
                publish_time = re.search(r'pubFinishTime=([0-9]+)', line)
                pub_start_time = re.search(r'beginPub=([0-9]+)', line)
                pub_finish_time = re.search(r'finishPub=([0-9]+)', line)
                fast_info = re.search(r'fast_push_id":([0-9]+)', line)
                if args.first:
                    cache[track_id.group(1)] = 1
                match = re.search(r'"meta_info":{.*}', line)
                if match:
                    match_string = match.group()[:len(match.group()) - 1]
                    match = re.search(r'{.*}', match_string)
                    if match:
                        d = json.loads(s=match.group())
                        if publish_time:
                            d['pubFinishTime'] = publish_time.group(1)
                        if pub_start_time:
                            d['beginPub'] = pub_start_time.group(1)
                        if pub_finish_time:
                            d['finishPub'] = pub_finish_time.group(1)
                        if fast_info:
                            if int(fast_info.group(1)) <= 0 or int(
                                    fast_info.group(1)) > 3:
                                miss_fast_3_count += 1
                        temp = get_duration_02(d)
                        if not temp:
                            continue
                        count += 1
                        for i in range(len(temp)):
                            if temp[i] < res_min[i]:
                                res_min[i] = temp[i]
                            if temp[i] > res_max[i]:
                                res_max[i] = temp[i]
                                res_max_info[i] = line
                            res_avg[i] += temp[i]

    for i in range(len(res_avg)):
        if count != 0:
            res_avg[i] /= count

    print_res(res_min, "min", suffix02)
    print_res(res_max, "max", suffix02)
    print_res(res_avg, "avg", suffix02)
    print("total: {}, miss-fast-3: {}".format(count, miss_fast_3_count))

    with open(max_results_file, 'w') as f:
        f.write("")

    with open(max_results_file, 'a') as f:
        for i in range(len(suffix02)):
            f.write("{} {}={}: {}".format("max", suffix02[i], res_max[i],
                                          res_max_info[i]))
    return res_min, res_max, res_avg


def normJson(line):
    line = line.replace('\\', '')
    line = line.replace('"{', '{')
    line = line.replace('}"', '}')
    return line


def print_res(results, prefix, suffix):
    for i in range(len(suffix)):
        print("{} {}: {} ms".format(prefix, suffix[i], results[i]))
    print('\n')


def get_duration_05(results):
    res = [0 for x in range(8)]
    res[0] = int(results['DecodeTime']) - int(results['RecvTime'])
    res[1] = int(results['AnalyzeTime']) - int(results['DecodeTime'])
    res[2] = int(results[args.item]) - int(results['AnalyzeTime'])
    res[3] = int(results['SearchFinishTime']) - \
        int(results[args.item])
    res[4] = int(results['PassAggregatorTime']) - \
        int(results['SearchFinishTime'])
    res[5] = int(results['StoreFinishTime']) - \
        int(results['PassAggregatorTime'])
    res[6] = int(results['PubTime']) - int(results['StoreFinishTime'])
    res[7] = int(results['PubTime']) - int(results['RecvTime'])
    return res


def get_duration_02(results):
    res = [0 for x in range(5)]
    res[0] = int(results['packetDecodeTime'])
    res[1] = int(results['CSDKRecvTime']) - res[0]
    if 'beginPub' in results and 'finishPub' in results:
        res[3] = int(results["finishPub"]) - int(results['beginPub'])
        if 'pubStartTime' in results:
            res[2] = int(results['pubStartTime']) - \
                int(results['CSDKRecvTime']) - \
                int(results['packetRecvTime'])
        res[4] = int(results['beginPub']) - int(results['pubStartTime'])
    # if res[2] < 0:
    #     print(parseRFC3339Nano(results['pubTime']).timestamp()*1000,
    #           int(results['packetRecvTime']))
    return res


# def parseRFC3339Nano(time):
#     pattern = r'([0-9]{4})-([0-9]{2})-([0-9]{2})T' + \
#         r'([0-9]{2}):([0-9]{2}):([0-9]{2})' + \
#         r'(\.([0-9]+))?(Z|([+-][0-9]{2}):([0-9]{2}))'
#     broken = re.search(pattern, time)
#     return(datetime.datetime(
#         year=int(broken.group(1)),
#         month=int(broken.group(2)),
#         day=int(broken.group(3)),
#         hour=int(broken.group(4)),
#         minute=int(broken.group(5)),
#         second=int(broken.group(6)),
#         microsecond=int(broken.group(8) or "0") // 1000,
#         tzinfo=datetime.timezone(datetime.timedelta(
#             hours=int(broken.group(10) or "0"),
#             minutes=int(broken.group(11) or "0")))))


def plot_result_02(res_min, res_max, res_avg):
    plt.style.use('Solarize_Light2')
    x = list(range(len(res_min)))
    total_width, n = 0.9, 3
    width = total_width / n
    x = [i - (total_width - width) / 2 for i in x]
    rects1 = plt.bar(x, height=res_min, label='min', width=width / 2)
    rects2 = plt.bar([i + width for i in x],
                     height=res_max,
                     label='max',
                     width=width / 2,
                     tick_label=suffix02)
    rects3 = plt.bar([i + 2 * width for i in x],
                     height=res_avg,
                     label='avg',
                     width=width / 2)
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2,
                 height + 1,
                 str(round(height, 1)),
                 ha="center",
                 va="bottom")
    for rect in rects2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2,
                 height + 1,
                 str(round(height, 1)),
                 ha="center",
                 va="bottom")
    for rect in rects3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2,
                 height + 1,
                 str(round(height, 1)),
                 ha="center",
                 va="bottom")
    plt.legend()
    plt.show()


def main():
    if args.version == '02':
        res_min, res_max, res_avg = parse02(args.logfile)
        if args.plot:
            plot_result_02(res_min, res_max, res_avg)
    elif args.version == '05':
        parse05(args.logfile)


if __name__ == "__main__":
    main()
