#!/usr/bin/env python3

import config
import pathlib
import threading
import subprocess


try:
    # TODO: remove in v2.0
    config.downloads = config.dl_path
    print("WARNING: configuration parameter dl_path is deprecated.", flush=True)
    print("Please update to downloads", flush=True)
    # TODO: remove in v3.0
    # print("ERROR: configuration parameter dl_path has been removed.", flush=True)
    # print("Please update to downloads", flush=True)
    # exit(1)
except AttributeError:
    pass

def termy(cmd):
    output = []
    task = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in iter(task.stdout.readline, ""):
        out = line.decode('utf-8')
        if out != '':
            output.append(out)
            if config.debug is True:
                print(out, flush=True)
        if task.poll() != None:
            break
    err = task.stderr.read().decode('utf-8')
    print(err, flush=True)
    if config.debug is True:
        output = ''.join(output)
        print(output, flush=True)
    print(f"Finished downloading {cmd[-1]}", flush=True)

def dl(url):
    print(f"Downloading {url} (youtube-dl)...")
    cmd = [
        '/usr/bin/python3', '/usr/local/bin/youtube-dl', '-w',
        '-f', '(bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best)',
        '--merge-output-format', 'mp4',
        '-o', pathlib.Path(config.downloads, '%(title)s.%(ext)s'),
        url
    ]
    t = threading.Thread(target=termy, args=(cmd,))
    t.start()

# TODO: implement and test config files
def ytdlp(url):
    print(f"Downloading {url}...", flush=True)
    cmd = [
        'yt-dlp',
        '-P', f'home:{config.downloader_configs}',
        '-P', f'temp:{config.downloads_tmp}',
        '-P', f'{config.downloads}',
        '--windows-filenames',
        '-f', 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b',
        url
    ]
    if config.debug is False:
        cmd.insert(1, '-q')
    t = threading.Thread(target=termy, args=(cmd,))
    t.start()
