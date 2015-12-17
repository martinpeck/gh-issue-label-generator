# GitHub Issue Label Generator

This python script will generate the standard set of labels that we use in all of our GitHub issues databases.

The definition of the lables you want to create is set within `definitions.json`. The script expects all existing labels to have already been deleted. Errors will be generated if the label it's trying to create already exists. The script will carry on, but it won't overwrite/modify the existing label.

## Usage ##

- set up a virtual environment (because I said so)
- install the requirements with `pip install -r requirements.txt`
- make sure that ALL of the existing labels in the repository are deleted (or, be prepared to put up with some errors)
- run `gen-labels.py` in the following manner...

```
python gen-labels.py -u USERNAME -p PASSWORD -o REPOSITORY-OWNER -r REPOSITORY
```

For example...

```
python gen-labels.py -u martinpeck -p 1234$abcd -o martinpeck -r plinky

```

Full usage can be obtained by using `-h` command line arg...

```
usage: gen-labels.py [-h] -u USERNAME -p PASSWORD -o OWNER -r REPOSITORY
                     [-d DEFINITIONS] [-t]

Generates GitHub issue labels.

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --user USERNAME
                        github username
  -p PASSWORD, --pass PASSWORD
                        github password, or application token for 2FA
  -o OWNER, --owner OWNER
                        the owner of the repository to update
  -r REPOSITORY, --repo REPOSITORY
                        the repository to update
  -d DEFINITIONS, --def DEFINITIONS
                        location of json file containing label definitions.
                        Defaults to definitions.json
  -t, --test            If true, performs a dry run without actually making
                        request to github
```

## Limitations ##

Issues are all tracked in GitHub Issues...using labels that I created with this script! There are a few enhancements I'd like to make, but feel free to post issues as and when you find them...or, better still, send me a pull request.


