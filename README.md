# Saurida fuel prices API

Saurida fuel prices in Lithuania. A poor man's API.

# Usage

## CLI

You can easily get price using below request in bash (see [prices.json](https://github.com/erkexzcx/saurida-fuel-prices/blob/main/prices.json) for more details):
```bash
curl -s https://raw.githubusercontent.com/erkexzcx/saurida-fuel-prices/main/prices.json | jq '.alytus_miskininku_g.dyzelinas_b7'
```

## Home Assistant integration

Update `configuration.yml` and add below code (see [prices.json](https://github.com/erkexzcx/saurida-fuel-prices/blob/main/prices.json) for more details):
```yaml
sensor:
  - platform: rest
    scan_interval: 3600 # 1 hour
    resource: "https://raw.githubusercontent.com/erkexzcx/saurida-fuel-prices/main/prices.json"
    name: "Saurida Alytus, Miškininkų g. diesel price"
    value_template: '{{ value_json.alytus_miskininku_g.dyzelinas_b7 }}'
    force_update: True
    icon: "mdi:gas-station"
    unit_of_measurement: "€/l"
```
