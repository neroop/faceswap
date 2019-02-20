# -*- coding: UTF-8 -*-

import pandas as pds
import os

"""
截取指定时间区间的视频

ffmpeg  -ss 1 -i URE-047.mp4 -t 1 -c:v libx264 -pix_fmt yuv420p ~/Downloads/Images/zsa/URE-047_1.mp4
"""

fan_code = 'MIDD-913'
video_fmt = '.wmv'
input_base = '/Users/zhou/Movies/.Mov/佐山爱'
output_base = '/Users/zhou/Downloads/images/'

input_ = os.path.join(input_base, fan_code + video_fmt)
cmd = 'ffmpeg -ss {start} -i {input} -t {length} -c:v libx264 -pix_fmt yuv420p {output}'

duration_csv = os.path.join('/Users/zhou/', fan_code + '.csv')
data_frame = pds.read_csv(duration_csv)

for it, ss, ed in zip(data_frame.i, data_frame.b, data_frame.e):
    output = os.path.join(output_base, fan_code + "_" + str(it) + video_fmt)

    def time_to_second(time_str):
        tokens = time_str.split(":")
        seconds = 0
        for i, token in enumerate(reversed(tokens)):
            seconds += 60**i * int(token)
        return seconds

    start = time_to_second(ss)
    length = max(1, time_to_second(ed) - start)

    cur_cmd = cmd.format(input=input_, output=output, start=start, length=length)
    print(cur_cmd)
    os.system(cur_cmd)