import json
from datetime import datetime, timedelta
import random
import argparse

def generate_sample_json(num_events):
    base_timestamp = datetime.now() - timedelta(hours=2)
    json_data = []

    for i in range(num_events):
        timestamp = base_timestamp + timedelta(minutes=i)
        event = {
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "translation_id": f"{random.randint(100000, 999999)}",
            "source_language": "en",
            "target_language": "fr",
            "client_name": "airliberty",
            "event_name": "translation_delivered",
            "duration": random.randint(10, 60),
            "nr_words": random.randint(10, 100)
        }
        json_data.append(event)

    return json_data

def write_json(output_file, json_data):
    with open(output_file, 'w') as file:
        json.dump(json_data, file, indent=2)




def main():
    parser = argparse.ArgumentParser(description='Unbabel Challange Event Generator')
    parser.add_argument('--file_name', type=str, default='events.json', help='File name for the output file', required=False)
    parser.add_argument('--n_events', type=int, default=100, help='Number of events to generate', required=False)
    args = parser.parse_args()


    file_name = args.file_name
    n_events = args.n_events
    json_data = generate_sample_json(n_events)
    write_json(file_name, json_data)

    print(f"Generated {n_events} events and saved to {file_name}.")

main()
