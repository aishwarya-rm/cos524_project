#!/bin/bash
[[ "$1" =~ ^https://dl.acm.org/doi/.* ]] || (sleep 1 && curl -i $1 -I  | grep -Eo "https://dl.acm.org/doi/(abs/)?[0-9./]+")


