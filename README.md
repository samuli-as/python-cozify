# cozify-temp
Pull Proove multisensor data from Cozify Hub into InfluxDB

For now to get the required hub-key have a look at: https://bitbucket.org/mikakolari/cozify

## installation
- cp main.cfg.dist main.cfg
- edit main.cfg to contain your hub ip address and hub key
- run cozify-temp.py to get a single snapshot and push it to InfluxDB. Loop it to get continuous data.

![example Grafana graphs][graphs]

[graphs]: https://i.imgur.com/TwrfXES.png "example Grafana graphs"
