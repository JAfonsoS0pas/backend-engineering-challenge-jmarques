import json
import argparse
from datetime import datetime, timedelta


CALCULATION_TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
RESULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def read_json(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    return data



def calculate_moving_average(json_data, window_size):
    #extract all timestamps and durations
    timestamps = [datetime.strptime(event["timestamp"], CALCULATION_TIME_FORMAT) for event in json_data]
    duration = [event["duration"] for event in json_data]

    #finds earliest timestamp and rounds it to the minute previous
    current_timestamp = min(timestamps).replace(second=0).replace(microsecond=0)
    #finds latest timestamp and rounds it to the next minute
    end_timestamp = max(timestamps).replace(second=0).replace(microsecond=0)+timedelta(minutes=1)
    moving_averages = []

    while current_timestamp <= end_timestamp:

        #all events that fall within the window size
        relevant_events = [
            delivery_time
            for timestamp, delivery_time in zip(timestamps, duration)
            if current_timestamp - timedelta(minutes=window_size) < timestamp <= current_timestamp
        ]

        #calculate the moving average
        if relevant_events:
            average_delivery_time = sum(relevant_events) / len(relevant_events)
        #if no values are found the average is 0
        else:
            average_delivery_time = 0
        
        moving_averages.append({"timestamp": current_timestamp.strftime(RESULT_TIME_FORMAT), "moving_average": average_delivery_time})

        current_timestamp += timedelta(minutes=1)

    return moving_averages


def generate_file(moving_averages, output_file):
    with open(output_file, 'w') as file:
            json.dump(moving_averages, file, indent=2)


def main():
    #set input arguments
    parser = argparse.ArgumentParser(description='Unbabel Challange')
    parser.add_argument('--input_file', type=str, help='Path to the input JSON file', required=True)
    parser.add_argument('--window_size', type=int, help='Window size for sorting (in minutes)', required=True)
    parser.add_argument('--output_file', type=str, default='results.json', help='File name for the output file', required=False)
    args = parser.parse_args()

    input_file = args.input_file
    window_size = args.window_size
    output_file = args.output_file

    #read json file
    json_data = read_json(input_file)

    #calculate moving averages
    moving_averages = calculate_moving_average(json_data, window_size)

    generate_file(moving_averages, output_file)

    


main()