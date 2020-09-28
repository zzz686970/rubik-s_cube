from google.cloud import bigquery

client = bigquery.Client()

query_job = client.query("""
    #standardSQL
    SELECT *
    FROM `dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export`
    """)

results = query_job.result()  # Waits for job to complete.

for row in results:
    print("{}: {}".format(row.title, row.unique_words))