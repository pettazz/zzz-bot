import datetime, time
import fitbit

import config

start = datetime.datetime.now()
authd_client = fitbit.Fitbit(
    config.FITBIT.client_id, 
    config.FITBIT.client_secret,
    access_token = config.FITBIT.access_token,
    refresh_token = config.FITBIT.refresh_token)

while True:
    elapsed = datetime.datetime.now() - start
    if elapsed > datetime.timedelta(days=1):
        authd_client.log_sleep(datetime.datetime.now() - datetime.timedelta(days=0), 27000000)
        start = datetime.datetime.now()
    else:
        time.sleep(3600)