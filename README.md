# EZ Takeout

EZ Takeout is a course project aimed for Uber & Yelp combined analytics and application
  - EECS 6893 Big Data Analytics
  - Team **Yulong Qiao yq2212**, **Yang Chen yc3313** and **Xiyan Liu xl2672**

## Project Structure

    EZTakeout
    ├── EZTakeoutApp
    │   ├── 2016-06.amount.pkl
    │   ├── 2016-06.time.pkl
    │   ├── 2016-07.amount.pkl
    │   ├── 2016-07.time.pkl
    │   ├── 2016-09.amount.pkl
    │   ├── 2016-09.time.pkl
    │   ├── 2016-10.amount.pkl
    │   ├── 2016-10.time.pkl
    │   ├── 2016-11.amount.pkl
    │   ├── 2016-11.time.pkl
    │   ├── 2016-12.amount.pkl
    │   ├── 2016-12.time.pkl
    │   ├── 2017-01.amount.pkl
    │   ├── 2017-01.time.pkl
    │   ├── 2017-02.amount.pkl
    │   ├── 2017-02.time.pkl
    │   ├── 2017-03.amount.pkl
    │   ├── 2017-03.time.pkl
    │   ├── 2017-04.amount.pkl
    │   ├── 2017-04.time.pkl
    │   ├── 2017-05.amount.pkl
    │   ├── 2017-05.time.pkl
    │   ├── 2017-06.amount.pkl
    │   ├── 2017-06.time.pkl
    │   ├── Gruntfile.js
    │   ├── app
    │   │   ├── 404.html
    │   │   ├── images
    │   │   │   └── loading.gif
    │   │   ├── index.html
    │   │   ├── robots.txt
    │   │   ├── scripts
    │   │   │   ├── app.js
    │   │   │   └── controllers
    │   │   │       ├── index.js
    │   │   │       └── map.js
    │   │   ├── styles
    │   │   │   ├── index.css
    │   │   │   └── map.css
    │   │   └── views
    │   │       ├── index.html
    │   │       └── map.html
    │   ├── app.js
    │   ├── bower.json
    │   ├── config.json
    │   ├── exec.sh
    │   ├── model_predict.py
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── test
    │   │   ├── karma.conf.js
    │   │   └── spec
    │   │       └── controllers
    │   │           ├── about.js
    │   │           └── main.js
    │   ├── trip_distance.linear_regression_model.amount.pkl
    │   └── trip_distance.linear_regression_model.time.pkl
    ├── EZTakeout_TeamI194_Final\ Pre.pdf
    ├── README.md
    ├── model
    │   ├── 2016-06.amount.pkl
    │   ├── 2016-06.time.pkl
    │   ├── 2016-07.amount.pkl
    │   ├── 2016-07.time.pkl
    │   ├── 2016-09.amount.pkl
    │   ├── 2016-09.time.pkl
    │   ├── 2016-10.amount.pkl
    │   ├── 2016-10.time.pkl
    │   ├── 2016-11.amount.pkl
    │   ├── 2016-11.time.pkl
    │   ├── 2016-12.amount.pkl
    │   ├── 2016-12.time.pkl
    │   ├── 2017-01.amount.pkl
    │   ├── 2017-01.time.pkl
    │   ├── 2017-02.amount.pkl
    │   ├── 2017-02.time.pkl
    │   ├── 2017-03.amount.pkl
    │   ├── 2017-03.time.pkl
    │   ├── 2017-04.amount.pkl
    │   ├── 2017-04.time.pkl
    │   ├── 2017-05.amount.pkl
    │   ├── 2017-05.time.pkl
    │   ├── 2017-06.amount.pkl
    │   ├── 2017-06.time.pkl
    │   ├── ETL
    │   │   ├── count.txt
    │   │   ├── find_columbia.py
    │   │   ├── month_day_reducer.py
    │   │   ├── trip_data_clean.py
    │   │   ├── trip_data_extraction.py
    │   │   ├── utils.py
    │   │   └── yelp_retrieval.py
    │   ├── Reviews_Stars.ipynb
    │   ├── datasets
    │   │   └── processed
    │   │       ├── tripdata
    │   │       │   └── dummy.txt
    │   │       └── tripdata_reduced
    │   │           └── dummy.txt
    │   ├── exec.sh
    │   ├── graphs
    │   │   ├── distance-cost-predict_by_months.png
    │   │   ├── distance-cost-predict_by_months_overall.png
    │   │   ├── distance-cost-predict_by_overall_with_hours.png
    │   │   ├── distance-time-predict_by_months.png
    │   │   ├── distance-time-predict_by_months_overall.png
    │   │   ├── distance-time-predict_by_overall_with_hours.png
    │   │   ├── distance_time_scatter.png
    │   │   ├── stars-reviews.LR.png
    │   │   ├── stars-reviews.png
    │   │   └── wordcloud.jpg
    │   ├── hours_compare_to_overall.py
    │   ├── model_predict.py
    │   ├── month_compare_to_overall.py
    │   ├── train_trip_model.py
    │   ├── trip_distance.linear_regression_model.amount.pkl
    │   └── trip_distance.linear_regression_model.time.pkl
    ├── pkl
    │   ├── 2016-06.amount.pkl
    │   ├── 2016-06.time.pkl
    │   ├── 2016-07.amount.pkl
    │   ├── 2016-07.time.pkl
    │   ├── 2016-09.amount.pkl
    │   ├── 2016-09.time.pkl
    │   ├── 2016-10.amount.pkl
    │   ├── 2016-10.time.pkl
    │   ├── 2016-11.amount.pkl
    │   ├── 2016-11.time.pkl
    │   ├── 2016-12.amount.pkl
    │   ├── 2016-12.time.pkl
    │   ├── 2017-01.amount.pkl
    │   ├── 2017-01.time.pkl
    │   ├── 2017-02.amount.pkl
    │   ├── 2017-02.time.pkl
    │   ├── 2017-03.amount.pkl
    │   ├── 2017-03.time.pkl
    │   ├── 2017-04.amount.pkl
    │   ├── 2017-04.time.pkl
    │   ├── 2017-05.amount.pkl
    │   ├── 2017-05.time.pkl
    │   ├── 2017-06.amount.pkl
    │   ├── 2017-06.time.pkl
    │   ├── trip_distance.linear_regression_model.amount.pkl
    │   └── trip_distance.linear_regression_model.time.pkl
    └── requirements.txt


### Data Sources

 - 100 million lines 1-year Jun. 2016 - Jun. 2017[New York Taxi Data]
 - 4.7 million lines [Yelp DataSet]

### Explanations and Instructions

#### Analytics

1. Refer to `requirements.txt`, use `virtualenv` to load all necessary python packages
2. Download all datasets, both taxi datasets & yelp datasets into **[raw]** folder
3. Command into [ETL] folder, execute `trip_data_clean.py` and `trip_data_extraction.py` to generate all necessary extracted datasets in [tripdata]
4. Use Spark `spark-submit month-day-reducer.py` to generate all reduced datasets in [tripdata_reduced]
5. Find `hours_compare_to_all.py`, `month_compare_to_overall.py`, `Reviews_Stars.ipynb` in [model] folder, execute these to see all analytical graphs

#### Application

1. Make sure you have `npm` and `bower` properly installed
2. Command into [EZTakeoutApp]
3. run `npm install && bower install`
4. execute `mv bower_components app/bower_components`
5. run `npm start`

You can also ignore 3-5 steps by simply execute `bash exec.sh`


[New York Taxi Data]:<http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml>
[Yelp DataSet]:<https://www.yelp.com/dataset/challenge>
[raw]:<https://github.com/youleer727/EZTakeout/tree/master/model/datasets/raw>
[ETL]:<https://github.com/youleer727/EZTakeout/tree/master/model/ETL>
[tripdata]:<https://github.com/youleer727/EZTakeout/tree/master/model/datasets/processed/tripdata>
[tripdata_reduced]:<https://github.com/youleer727/EZTakeout/tree/master/model/datasets/processed/tripdata_reduced>
[model]:<https://github.com/youleer727/EZTakeout/tree/master/model>
[EZTakeoutApp]:<https://github.com/youleer727/EZTakeout/tree/master/EZTakeoutApp>