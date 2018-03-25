#!/usr/bin/env bash
ndir=$(cd `dirname $0`; pwd)
rsync -avP $ndir/* -avP 10.0.83.147:/root/HouseCrawler/