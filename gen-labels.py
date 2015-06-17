import requests
import argparse
import json
import collections

def output(message):
  print(message)

def setup_args_parser():
  parser = argparse.ArgumentParser(description="Generates GitHub issue labels.")
  parser.add_argument('-u', '--user', dest='username', required = True, help="github username")
  parser.add_argument('-p', '--pass', dest='password', required = True, help="github password, or application token for 2FA")
  parser.add_argument('-o', '--owner', dest='owner', required = True, help="the owner of the repository to update")
  parser.add_argument('-r', '--repo', dest='repository', required = True, help="the repository to update")
  parser.add_argument('-d', '--def', dest='definitions', help="location of json file containing label definitions. Defaults to definitions.json", default='definitions.json')
  parser.add_argument('-t', '--test', dest='test', action='store_true', help="If true, performs a dry run without actually making request to github")
  return parser

def parse_args():
  output("parsing arguments")
  return setup_args_parser().parse_args()

def read_definitions(file):
  output("reading defintions from file " + file)
  with open(args.definitions) as stream:
    return json.load(stream)

def generate_request(args, label_def):
  url = "https://api.github.com/repos/%s/%s/labels" % (args.owner, args.repository)
  body = json.dumps({'name':label_def['name'], 'color': label_def['color']})
  return (url, body)

def print_progress(name, color, request):
  output("  " + name + ", " + color + ", " + request)

def test_output(args, label_defs):
  output("This will generate the following labels, using HTTP requests:")
  for label_def in label_defs['label']:
    print_progress(label_def['name'], label_def['color'], generate_request(args, label_def)[0])

def issue_requests(args, label_defs):
  output("Creating labels:")
  for label_def in label_defs['label']:
    name = label_def['name']
    color = label_def['color']
    output("  creating '%s' with color '%s'" % (label_def['name'], label_def['color']))

    auth = (args.username, args.password)
    http_request = generate_request(args, label_def)
    response = requests.post(http_request[0], data=http_request[1], auth=auth, timeout=10)

    if (response.status_code != 200 and response.status_code != 201):
      output("  failed: (%s) %s" % (response.status_code, response.text))
    else:
      output("  done (%s)!" % (response.status_code))

if __name__ == '__main__':

  args = parse_args()
  label_defs = read_definitions(args.definitions)

  if args.test:
    test_output(args, label_defs)
  else:
    issue_requests(args, label_defs)
