#!/usr/bin/env python3
import os
import config
import threading
import subprocess


def termy(cmd):
    output = []
    task = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in iter(task.stdout.readline, ""):
        out = line.decode('utf-8')
        if out != '':
            output.append(out)
            print(out)
        if task.poll() != None:
            break
    err = task.stderr.read().decode('utf-8')
    output = ''.join(output)
    print(err, flush=True)
    return output, err

def dl(url):
    print("Downloading {}".format(url))
    cmd = [
        '/usr/bin/python3', '/usr/local/bin/youtube-dl', '-w',
        '-f', '(bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best)',
        '--merge-output-format', 'mp4',
        '-o', os.path.join(config.dl_path, '%(title)s.%(ext)s'),
        url
    ]
    t = threading.Thread(target=termy, args=(cmd,))
    t.start()
