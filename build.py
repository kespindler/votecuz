from jinja2 import Environment, FileSystemLoader
import yaml
import os.path as op
import os

OUTPUT_DIR = 'docs/'
LINK_LENGTH = len('bit.ly/123456')
HASHTAG_LEN = len('#votecuz')
MAX_LENGTH = 140 - LINK_LENGTH - HASHTAG_LEN - 2



def write(template, config, out_path):
    body = template.render(**config)
    out_dir = op.join(OUTPUT_DIR, out_path)
    if out_path is not '.':
        os.mkdir(out_dir)
    with open(op.join(out_dir, 'index.html'), 'w') as f:
        f.write(body)


def build(base_config):
    loader = FileSystemLoader('templates')
    env = Environment(loader=loader)
    template = env.get_template('index.j2')

    write(template, base_config, '.')

    template = env.get_template('issue.j2')
    for reason in base_config['reasons']:
        assert len(reason['tagline']) <= MAX_LENGTH, (
            'length of %s must be less than %d' % (
                reason['title'], MAX_LENGTH)
            )
                
        conf = dict(**base_config)
        conf['reason'] = reason
        write(template, conf, reason['tag'])


def update_config(base_config):
    for reason in base_config['reasons']:
        reason['tag'] = reason['title'].lower().replace(' ', '-')
    return base_config


def main():
    config = yaml.load(open('reasons.yaml'))
    config = update_config(config)
    build(config)


if __name__ == '__main__':
    main()
