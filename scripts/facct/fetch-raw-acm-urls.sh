#!/bin/bash
curl https://facctconference.org/2021/acceptedpapers.html https://facctconference.org/2020/acceptedpapers.html https://facctconference.org/2019/acceptedpapers.html | grep -Eo "https://dl.acm.org/(doi/(abs/)?[0-9./]+|authorize\?N[0-9]+)"

