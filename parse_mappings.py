"""Module for parsing yaml mappings file to dotenv file for exporting environment variables in jobs

"""
import sys
import yaml
import argparse


def read_config(path):
    """Read yaml config

    Args:
        path (string): path to config file

    Returns:
        dict: config as dict
    """
    with open(path, 'r') as file:
        conf = yaml.safe_load(file)

    return conf


def get_nested_key_vals(conf, keys):
    """Get nested key value of the configuration

    Args:
        conf (dict): mappings config dict
        keys (list): nested keys

    Returns:
        env_vars (dict): nested dict of env vars to be exported
    """

    env_vars_dict = conf
    for key in keys:
        env_vars_dict = env_vars_dict[key]

    return env_vars_dict


def export_vars(env_vars_dict):
    """Export to dotenv file

    Args:
        env_vars_dict (dict): key values to be exported as env vars in dotenv file
    """
    env_vars = ['{}={}'.format(k, env_vars_dict[k])
                for k in env_vars_dict.keys()]
    with open("vars.env", "w") as file:
        for item in env_vars[:-1]:
            file.write("{}\n".format(item))
        file.write("{}".format(env_vars[-1]))


def main():
    """Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", type=str, help="Path to the mappings file with .yaml extension")
    parser.add_argument('--keys', type=str,
                        help="Nested keys in yaml file to export its child values to the dotenv file (vars.env)",
                        nargs='+', required=True)
    args = parser.parse_args()
    env_vars_dict = get_nested_key_vals(read_config(
        args.path), args.keys)
    export_vars(env_vars_dict)


main()
