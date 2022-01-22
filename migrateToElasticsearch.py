#!/usr/bin/python3

import json
import os

import psycopg2
from OSINTmodules import *

esAddress = os.environ.get('ELASTICSEARCH_URL') or "http://localhost:9200"
esClient = OSINTelastic.elasticDB(esAddress, "osinter_articles")


conn = psycopg2.connect("dbname=osinter user=postgres")

columns = ["id", "title", "description", "url", "image_url", "author", "publish_date", "profile", "scraped", "inserted_at", "file_path"]

with conn.cursor() as cur:

    cur.execute(f"SELECT {', '.join(columns)} FROM articles")

    dbArticles = cur.fetchall()

    print(len(dbArticles))

    for article in dbArticles:
        articleDetails = {descriptor:value for (descriptor,value) in zip(columns, article)}

        articleContents = []
        with open(f"{articleDetails['file_path']}.md") as contentsFile:
            start = False
            line = contentsFile.readline()
            while line:
                line = contentsFile.readline()

                if line.startswith("## Article:"):
                    start = True
                
                if line.startswith("## Tags:"):
                    break

                if start:
                    articleContents.append(line)

        articleDetails["contents"] = "".join(articleContents)

        with open(f"./OSINTprofiles/profiles/{articleDetails['profile']}.profile") as profileFile:
            currentProfile = json.load(profileFile)

        articleDetails["source"] = currentProfile["source"]["name"]

        for unwantedProperty in ["scraped", "file_path"]:
            articleDetails.pop(unwantedProperty)

        currentArticle = OSINTobjects.Article(**articleDetails)

        if not esClient.existsInDB(currentArticle.url):
            esClient.saveArticle(currentArticle)
