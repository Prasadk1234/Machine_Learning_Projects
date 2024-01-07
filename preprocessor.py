import re
import pandas as pd


def preprocess(data):
    # pattern
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    # messages
    message = re.split(pattern, data)[1:]
    # dates
    dates = re.findall(pattern, data)
    # covert message into DataFrame
    df = pd.DataFrame({'user_message': message, 'message_date': dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Assuming 'df' is your DataFrame containing the 'user_message' column
    users = []
    messages = []

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split('([\w\W]):', message)
        if len(entry) > 1:  # Check if there's a user name and message
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('No One')
            messages.append(entry[0])

    # Assign the 'users' and 'messages' lists to new columns in the DataFrame
    df['user'] = users
    df['message'] = messages

    # Assign the 'users' and 'messages' lists to new columns in the DataFrame
    df['user'] = users
    df['message'] = messages

    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 2:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    return df
