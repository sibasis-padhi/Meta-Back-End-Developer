http_status = 200

if http_status == 200 or http_status == 201:
    print('Success!')
elif http_status == 400:
    print('Bad Request!')
elif http_status == 404:
    print('Not Found!')
elif http_status == 500:
    print('Internal Server Error!')
elif http_status == 503:
    print('Service Unavailable!')
elif http_status == 504:
    print('Gateway Timeout!')
else:
    print('Unknown Error!')

match http_status:
    case 200 | 201:
        print('Success!')
    case 400:
        print('Bad Request!')
    case 404:
        print('Not Found!')
    case 500:
        print('Internal Server Error!')
    case 503:
        print('Service Unavailable!')
    case 504:
        print('Gateway Timeout!')
    case _:
        print('Unknown Error!')