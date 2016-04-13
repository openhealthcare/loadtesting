# loadtesting

Loadtesting scripts and utilities for OHC projects

Our users like it when we make things that feel fast.

## Project: elCID@UCH

Effectively loadtesting elCID@UCH involves us creating realistic simulations of two components - our users, 
and the upstream data sources that we integrate with.

The user simulations are performed from the [Funkload](funkload.nuxeo.org/index.html) test cases in this 
repo, while the custom Gloss load tests live there (for now).

The funkload tests are configured in the file `elCID.conf`. This file sets the target hostname, as well as 
the number of concurrent users and length of cycles. Do consult the Funkload documentation, source code, or
conduct experiments for further detail.

To run: 

    cd ./gloss
    # Simulate upstream data for a duration of 8 minutes 
    # with a max throughput of 600 messages/second
    python gloss/tests/load_test.py -d 8 -t 600 
    
    # In a separate shell
    cd ./loadtesting
    # Runs the test_daily method of the class elCID in the file elcid_test.py
    fl-run-bench elcid_test.py elCID.test_daily
