#!/usr/bin/env python3

import sys
import subprocess


def runserver_bonjour(service_name, service_type, port):

  django_process = subprocess.Popen(
    ['python3', 'manage.py', 'runserver', '0.0.0.0:%s' % port],
    stdout=sys.stdout,
    stderr=sys.stderr)

  dns_process = subprocess.Popen(
    ['dns-sd', '-R', service_name, service_type, 'local', port],
    stdout=sys.stdout,
    stderr=sys.stderr)

  try:
    django_process.wait()
  except KeyboardInterrupt:
    print ('\nShutting down...')
  finally:
    dns_process.terminate()
    django_process.terminate()


if __name__ == '__main__':

  import argparse
  
  parser = argparse.ArgumentParser(description='Runs your Django project and publishes it using Bonjour. Should be run from the same folder as manage.py')
  parser.add_argument('--name', dest='service_name', help='Bonjour service name', default='Vortice Device')
  parser.add_argument('--type', dest='service_type', help='Bonjour service type', default='_vortice_config._tcp')
  parser.add_argument('--port', dest='port', help='port number for the Django server', default='8000')

  args = parser.parse_args(sys.argv[1:])    

  runserver_bonjour(args.service_name, args.service_type, args.port)