# Backend Engineering Challenge


Welcome to my sollution to the Engineering Challenge 🖖

In this repository 3 scripts can be found, the ```events_generator.py``` is a simple script to generate any number of random events for testing porpuses. The 2 remaining scripts are my solutions for this challange, please consider the ```unbabel_cli_optimized.py``` script as the main sollution for the challange, the ```unbabel_cli.py``` was an original sollution that was kept as a benchmark for the optimizations as well as a validator for the correctness of the optimized scripts output.

## How to run

Everything was done using Python 3.11.6 so you can use the python or python3 command to run the scripts

To run the generator script use 

	```python3 events_generator.py --file_name events.json --n_events 100```
 
the --file_name and --n_events are optional and will default to the values provided in the example command. Again this command is optional as in the repository there is already an events file with the example provided in the challange.

To run the remaing scripts use

	```python3 *script_name*.py --input_file events.json --window_size 10 --output_file results.json```
 
here the --input_file and --window_size flags are not optional and should be specified however the --output_file is optional and will default to results.json for the unoptimized script and results_optimized.json for the optimized script.

In Unix or Unix-like systems you can use time before each command to see the runtime of each script and evaluate the performance changes from the first iteration of the script to the last. Example:

	```time python3 unbabel_cli_optimize.py --input_file events.json --window_size 10 --output_file results_optimized.json```


 

## Challenge Scenario

At Unbabel we deal with a lot of translation data. One of the metrics we use for our clients' SLAs is the delivery time of a translation. 

In the context of this problem, and to keep things simple, our translation flow is going to be modeled as only one event.

### *translation_delivered*

Example:

```json
{
	"timestamp": "2018-12-26 18:12:19.903159",
	"translation_id": "5aa5b2f39f7254a75aa4",
	"source_language": "en",
	"target_language": "fr",
	"client_name": "airliberty",
	"event_name": "translation_delivered",
	"duration": 20,
	"nr_words": 100
}
```

## Challenge Objective

Your mission is to build a simple command line application that parses a stream of events and produces an aggregated output. In this case, we're interested in calculating, for every minute, a moving average of the translation delivery time for the last X minutes.

If we want to count, for each minute, the moving average delivery time of all translations for the past 10 minutes we would call your application like (feel free to name it anything you like!).

	unbabel_cli --input_file events.json --window_size 10
	
The input file format would be something like:

	{"timestamp": "2018-12-26 18:11:08.509654","translation_id": "5aa5b2f39f7254a75aa5","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 20}
	{"timestamp": "2018-12-26 18:15:19.903159","translation_id": "5aa5b2f39f7254a75aa4","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 31}
	{"timestamp": "2018-12-26 18:23:19.903159","translation_id": "5aa5b2f39f7254a75bb3","source_language": "en","target_language": "fr","client_name": "taxi-eats","event_name": "translation_delivered","nr_words": 100, "duration": 54}

Assume that the lines in the input are ordered by the `timestamp` key, from lower (oldest) to higher values, just like in the example input above.

The output file would be something in the following format.

```
{"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:13:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:14:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:15:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:22:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:23:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5}
```

#### Notes

Before jumping right into implementation we advise you to think about the solution first. We will evaluate, not only if your solution works but also the following aspects:

+ Simple and easy to read code. Remember that [simple is not easy](https://www.infoq.com/presentations/Simple-Made-Easy)
+ Comment your code. The easier it is to understand the complex parts, the faster and more positive the feedback will be
+ Consider the optimizations you can do, given the order of the input lines
+ Include a README.md that briefly describes how to build and run your code, as well as how to **test it**
+ Be consistent in your code. 

Feel free to, in your solution, include some your considerations while doing this challenge. We want you to solve this challenge in the language you feel most comfortable with. Our machines run Python (3.7.x or higher) or Go (1.16.x or higher). If you are thinking of using any other programming language please reach out to us first 🙏.

Also, if you have any problem please **open an issue**. 

Good luck and may the force be with you
