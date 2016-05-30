from flask import render_template, request
from staple_web import app
import yaml
import json


def get_yaml_files():
    i = 0
    yaml_files = []

    with open('energybalance.yaml', 'r') as stream:
        try:
            for yaml_file in yaml.load_all(stream):
                i += 1
                yaml_files.append((i, yaml_file))
        except yaml.YAMLError as exc:
            print(exc)

    return yaml_files


@app.route('/')
def index():
    yaml_files = get_yaml_files()

    return render_template('index.html', yaml_files=yaml_files)


@app.route('/export', methods=['POST'])
def on_export():
    data = request.get_json(force=True)
    with open('energybalance.yaml', 'w') as yml:
        yaml.safe_dump_all(data, yml, allow_unicode=True, default_flow_style=False)

    return ""


@app.route('/import', methods=['GET'])
def on_import():
    yaml_files = get_yaml_files()

    return json.dumps(yaml_files)
