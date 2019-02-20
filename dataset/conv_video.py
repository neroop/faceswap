# -*- coding: UTF-8 -*-

import os

"""
将视频转为图片


"""

video_fmt = '.wmv'
input_base = '/Users/zhou/Downloads/images/'
output_base = '/Users/zhou/Downloads/pics2/'
python_exec = '/Users/zhou/anaconda/envs/deepfake/bin/python'

cmd = '{python} tools.py effmpeg -i {input} -o {output}'

for filename in os.listdir(input_base):
    file = os.path.join(input_base, filename)
    if os.path.isfile(file):
        if file.endswith(video_fmt):
            cur_cmd = cmd.format(python=python_exec,
                                 input=file,
                                 output=output_base)
            print(cur_cmd)
            os.system(cur_cmd)
