#!/bin/bash
bundle exec jekyll liveserve &
sleep 10
open http://127.0.0.1:4000/
