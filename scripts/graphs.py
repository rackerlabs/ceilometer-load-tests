import argparse

import jinja2

template_loader = jinja2.FileSystemLoader(searchpath='.')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('graphs.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--graphite_server')
    parser.add_argument('-n', '--test_name')
    parser.add_argument('-f', '--from_value')
    parser.add_argument('-m', '--db_hostname', nargs='+')
    parser.add_argument('-d', '--db_datadisk', default='xvde')
    parser.add_argument('-w', '--db_network', default='eth1')
    parser.add_argument('-u', '--until_value', default=None)
    parser.add_argument('--mysql', action='store_true')
    parser.add_argument('--postgres', action='store_true')
    parser.add_argument('--mongo', action='store_true')
    args = parser.parse_args()
    template_args = {
        'graphite_server': args.graphite_server,
        'test_name': args.test_name,
        'from_value': args.from_value,
        'until_value': args.until_value,
        'db_hostnames': args.db_hostname,
        'db_graph_width': 800/len(args.db_hostname),
        'db_datadisk': args.db_datadisk,
        'db_network': args.db_network,
        'mysql': args.mysql,
        'postgres': args.postgres,
        'mongo': args.mongo
    }
    print template.render(template_args)