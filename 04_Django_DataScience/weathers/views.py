from django.shortcuts import render
from io import BytesIO
import matplotlib.pyplot as plt
import base64
import pandas as pd

csv_path = 'weathers/data/austin_weather.csv'

# Create your views here.
def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }
    return render(request, 'weathers/problem1.html', context)


def problem2(request):
    df = pd.read_csv(csv_path)
    
    df['Date'] = pd.to_datetime(df['Date'])

    plt.clf()

    plt.plot(df['Date'], df['TempHighF'], label='High Temp')
    plt.plot(df['Date'], df['TempAvgF'], label='Avg Temp')
    plt.plot(df['Date'], df['TempLowF'], label='Low Temp')

    plt.title('DAILY TEMP INFO')
    plt.xlabel('DATE')
    plt.ylabel('TEMP INFO')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart': f'data:image/png;base64,{image_base64}'
    }

    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    df = pd.read_csv(csv_path, usecols=['Date', 'TempHighF','TempAvgF', 'TempLowF'])

    df['Date'] = pd.to_datetime(df['Date'])
    df_avg = df.groupby(df['Date'].dt.strftime('%Y-%m')).mean()

    plt.clf()

    plt.plot(df_avg['Date'], df_avg['TempHighF'], label='High Temp')
    plt.plot(df_avg['Date'], df_avg['TempAvgF'], label='Avg Temp')
    plt.plot(df_avg['Date'], df_avg['TempLowF'], label='Low Temp')

    plt.title('MONTHLY TEMP INFO')
    plt.xlabel('DATE')
    plt.ylabel('TEMP INFO')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart': f'data:image/png;base64,{image_base64}'
    }
    return render(request, 'weathers/problem3.html', context)


def problem4(request):
    df = pd.read_csv(csv_path)

    events = {
        'No Events': 0,
        'Rain': 0,
        'Thunderstorm': 0,
        'Fog': 0,
        'Snow': 0,
    }

    for i in range(1, len(df['Date'])):
        evt = df['Events'][i]

        if evt == ' ':
            events['No Events'] += 1

        elif ',' in evt:
            evt_list = evt.split(' , ')

            for j in range(len(evt_list)):
                events[evt_list[j]] += 1

        else:
            events[evt] += 1

    x = ['No Events', 'Rain', 'Thunderstorm', 'Fog', 'Snow']
    y = [events['No Events'], events['Rain'], events['Thunderstorm'], events['Fog'], events['Snow']]

    plt.bar(x, y)

    plt.title('Weather Events')
    plt.xlabel('Events')
    plt.ylabel('Counts')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart': f'data:image/png;base64,{image_base64}'
    }
    return render(request, 'weathers/problem4.html', context)