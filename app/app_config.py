#!/usr/bin/env python3
import os
import configparser

def get_config():
    if os.path.isfile("ydl.conf"):
        config = read_config()
    else:
        config = create_config()
    
    if config:
        print_config(config)
        return(config)
    else:
        print("Error reading or creating config file, exiting...")
        exit(1)

def read_config():
    config = configparser.ConfigParser()
    config.read('ydl.conf')
    
    if config.has_option('app', 'flask_key') \
        and config.has_option('app', 'api_key') \
        and config.has_option('app', 'dl_path'):
        return({
            'api_key': config.get('app', 'api_key'),
            'flask_key':config.get('app', 'flask_key'),
            'dl_path':config.get('app', 'dl_path'),
        })
    else:
        return(None)

def create_config():
    import uuid
    
    print("Couldn't find config, creating a new one...")
    
    api_key = str(uuid.uuid4())
    flask_key = str(uuid.uuid4())
    
    default_config = {
        'api_key':api_key,
        'flask_key':flask_key,
        'dl_path':'/videos'
    }
    
    config = configparser.ConfigParser()
    config['app'] = default_config
    
    with open('ydl.conf', 'w') as file:
        config.write(file)
    
    return(default_config)

def print_config(config):
    print("Wrote new ydl.conf config file.")
    print(f"\tAPI key:   {config['api_key']}")
    print(f"\tFlask key: {config['flask_key']}")
    print(f"\tdl_path:   {config['dl_path']}")
    print("")
    

if __name__ == '__main__':
    get_config()
