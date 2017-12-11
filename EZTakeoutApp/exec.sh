#!/usr/bin/env bash
npm install
bower install
cd app
rm -rf bower_components
cd ../
mv bower_components app/bower_components
npm start