## Bigquery tasks
- [x] access required to download data
- [x] sql tasks
- [ ] visulization and insights

## Analyse historical time series data
This script downloads data from Alpha Vantage​[https://www.alphavantage.co/documentation/], extract closed price, and then visulize the data.
#### local run
```
pip install -r requirements.txt
python3 get_process_data.py
python3 app.py
```

#### deploy in docker
```
## cd into folder which has docker file
cd cryptocurrency
docker-compose up
## open browser
http://localhost:8050/
```

#### TODO
- [ ] CI/CD
 