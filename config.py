import toml

config = {"pathes": ["/hello", "/test"]}

tomlfile = open("config.toml", "w")
toml.dump(config, tomlfile)
tomlfile.close()