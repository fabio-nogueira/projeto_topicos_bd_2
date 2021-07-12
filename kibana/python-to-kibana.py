from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch()

with open('Date=2004-10-02.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='index2004')