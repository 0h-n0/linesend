import requests

def line_notify(line_token, message):
    endpoint = 'https://notify-api.line.me/api/notify'
    message = "\n{}".format(message)
    payload = {'message': message}
    headers = {'Authorization': 'Bearer {}'.format(line_token)}
    requests.post(endpoint, data=payload, headers=headers)
    print(f"Send your message: {message}")

def get_args():
    import argparse
    description = ('send a message from command line to LINE service.',
                   ' Before sending a message, You have to create your ',
                   'access token via https://notify-bot.line.me/my/.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-t', '--token',
                        action='store',
                        nargs='?',
                        const=None,
                        required=True,
                        type=str,
                        choices=None,
                        help=('set your LINE token.'),
                        metavar=None)
    parser.add_argument('-m', '--message',
                        action='store',
                        nargs='?',
                        const=None,
                        required=True,                        
                        type=str,
                        choices=None,
                        help=('set your message.'),
                        metavar=None)
                        
    return parser.parse_args()

def commandline():
    args = get_args()
    line_notify(args.token, args.message)
    
    
