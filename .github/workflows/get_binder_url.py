import yaml, os
with open('_config.yml') as fh:
    dictionary_data = yaml.safe_load(fh)
binder_url = dictionary_data['sphinx']['config']['html_theme_options']['launch_buttons']['binderhub_url']
outfile = open("binder_url", "w")
outfile.write(binder_url)
outfile.close()
