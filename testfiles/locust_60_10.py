from locust import HttpLocust, TaskSet, task, events, web
import time
import csv


def index(l):
    l.client.get("/")


class MyTaskSet(TaskSet):
    tasks = [index]


class MyLocust(HttpLocust):
    host = "http://www.example.com"
    result_file = "locust_experiment_result.csv"
    min_wait = 3000
    max_wait = 6000
    task_set = MyTaskSet
    header = ["timeStamp", "service", "type", "success", "responseTime", "bytes"]
    footer = ["http://www.example.com"]
    data = []
    last_entry = 0

    def __init__(self):
        super(MyLocust, self).__init__()
        events.request_success += self.save_succ
        events.request_failure += self.save_fail
        events.quitting += self.write

    def save_succ(self, request_type, name, response_time, response_length):
        self.save(request_type, name, response_time, response_length, 1)

    def save_fail(self, request_type, name, response_time):
        self.save(request_type, name, response_time, 0, 0)

    def save(self, request_type, name, response_time, response_length, success):
        timestamp = int(round(time.time() * 1000))
        if timestamp != self.last_entry:
            self.data.append([timestamp, name, request_type, success, response_time, response_length])
            self.last_entry = timestamp

    def write(self):
        with open(self.result_file, 'wb') as csv_file:
            csv_file.write(",".join(self.header) + "\n")
            for value in self.data:
                csv_file.write(",".join(str(x) for x in value) + "\n")
            csv_file.write(",".join(self.footer) + "\n")
