# pylint: disable=unused-variable

# app config #

# authentication API key when making requests
api_key = ''
# Flask's secret key
flask_key = ''

debug = False

# -- #


# paths #

# all paths should be absolute
# if using Docker, should be ignored and mapped using Docker

# where to place downloaded files
downloads = '/downloads'
# where to place download temp files
downloads_tmp = '/dl_tmp'
# where to place yt-dlp and youtube-dl config files
# reserved for the future, currently doesn't work
# downloader_configs = '/configs'

# -- #


#
# config setup, no touchy
#

import pathlib

downloads = pathlib.Path(downloads)
downloads_tmp = pathlib.Path(downloads_tmp)
downloader_configs = pathlib.Path(downloader_configs)

for path in [downloads, downloads_tmp, downloader_configs]:
    path.mkdir(parents=True, exist_ok=True)
