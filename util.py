import json
from anonymizer import Anonymizer
from faker import Faker
from faker.providers import internet
import re

anonymizer = Anonymizer()

def anonymize_url(url):
    identity = ('username','users','FirstName','lastName','LastName','FirstName','password','Password')
    for value in identity:
        if url.rfind(value) != -1:
            return replace(url, value)
    return url


def anonymize_ip():
    fake = Faker()
    fake.add_provider(internet)
    ip = fake.ipv4_private()
    return ip


def replace(url , string):
    position = url.rfind(string) + len(string) + 1
    substring = url[position:]
    anonymized_string = anonymizer.get_anonymized_name(substring)
    an_url = url.replace(substring, anonymized_string)
    #print(anonymizer.get_original_name(anonymized_string))
    return an_url


def parse_line(line):
    split_line = line.split(" ")
    if len(split_line) < 30:
        return []
    customer = {

    }
    customer.__setitem__("type", split_line[1])
    customer.__setitem__("timestamp", split_line[2])
    if "/" in split_line[3]:
        customer.__setitem__("elb_resource_id", split_line[3])
    else:
        split_line.insert(3,'dummy')
    ip = "'" + anonymize_ip() + "'"
    customer.__setitem__("client_ip", ip)
    customer.__setitem__("target_port", split_line[5])
    customer.__setitem__("request_processing_time", split_line[6])
    customer.__setitem__("target_processing_time", split_line[7])
    customer.__setitem__("response_processing_time", split_line[8])
    customer.__setitem__("elb_status_code", split_line[9])
    customer.__setitem__("target_status_code", split_line[10])
    customer.__setitem__("received_bytes", split_line[11])
    customer.__setitem__("sent_bytes", split_line[12])
    customer.__setitem__("http_method", split_line[13].replace('/', '').replace('"', ''))
    customer.__setitem__("uri", anonymize_url(split_line[14]))
    customer.__setitem__("http_version", split_line[15])
    customer.__setitem__("user_agent", split_line[16].replace('/', '').replace('"', ''))
    customer.__setitem__("ssl_cipher", split_line[17])
    customer.__setitem__("ssl_protocol", split_line[18])
    customer.__setitem__("target_group_arn", split_line[19])
    customer.__setitem__("trace_id", split_line[20])
    customer.__setitem__("domain_name", split_line[21])
    customer.__setitem__("chosen_cert_arn", split_line[22])
    customer.__setitem__("matched_rule_priority", split_line[24])
    customer.__setitem__("request_creation_time", split_line[25])
    customer.__setitem__("actions_executed", split_line[26])
    customer.__setitem__("redirect_url", split_line[27])
    customer.__setitem__("error_reason", split_line[28])
    target_ip = "'" + anonymize_ip() + "'"
    customer.__setitem__("target:port_list", target_ip)
    customer.__setitem__("target_status_code_list", split_line[30])
    customer.__setitem__("additonalLogs", " ")

    customer_json = json.dumps(customer,indent=2, sort_keys=False)
    return (customer_json)
