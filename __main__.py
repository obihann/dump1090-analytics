import argparse
import airlines


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dump1090 Analytics - Data from the SKY!!!')
    parser.add_argument('--force', default=False, action="store_true", help='Parse all data and override the time locks. This likely will create duplicate data.')
    parser.add_argument('--server', default="http://127.0.0.1", help="URL to dump1090 server")
    parser.add_argument('--port', default="8080", help="Port for the dump1090 server")
    args = parser.parse_args()

    airlines.check_the_sky(url=args.server, port=args.port, force=args.force)