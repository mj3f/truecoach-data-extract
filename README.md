# Truecoach Data Extract Script

This project was built to export JSON data from the truecoach API, since they have no built-in way to do it, and the data is 'mine'. However I see no reason why this script can't be modified to support other API data export operations, as the config that this script uses is not really truecoach-specific, apart from its use of Bearer tokens.

## Installation and running the script

First, clone this repo, cd into it and run `pip install -r requirements.txt`

Once the dependencies are installed, you'll need to create a `config.yaml` file (easiest way is to just rename the existing `example.config.yaml` file).
The config file is self-explanatory, you'll need to provide it with the APIs base url, a list of API endpoints that you want to target, and a Bearer token.

Once the `config.yaml` file is complete, simply run the script by executing `python extract.py` and the data should be written into a set of json files, one for each endpoint, and can be found within the `data/` directory within this repo.
