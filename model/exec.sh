#!/usr/bin/env bash
mkdir -p datasets/processed/tripdata
mkdir -p datasets/raw
python trip_data_clean.py
python trip_data_extraction.py