#!/usr/bin/env python3
import threading
import app_config
import subprocess


config = app_config.get_config()


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
    print(err)
    return(output, err)

# TODO: add videos path as a config item
def dl(url):
    print("Downloading {}".format(url.decode('utf-8')))
    cmd = [
        '/usr/bin/python3', '/usr/local/bin/youtube-dl', '-w',
        '-f', '(bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best)',
        '-o', os.path.join(config['dl_path'], '%(title)s.%(ext)s'),
        url.decode('utf-8')
    ]
    t = threading.Thread(target=termy, args=(cmd,), daemon=True)
    t.start()
