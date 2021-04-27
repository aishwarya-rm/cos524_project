#!/bin/bash
./scripts/facct/fetch-raw-acm-urls.sh | xargs -L1 ./scripts/facct/follow-redirect.sh | grep -Eo "10[0-9./]+$" | tee ./data/facct-doi.txt
