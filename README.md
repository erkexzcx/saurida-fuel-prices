# Saurida fuel prices

Saurida fuel prices in Lithuania. A poor man's API.

# Usage

## CLI

You can easily get price using below request in bash:
```bash
curl -s https://raw.githubusercontent.com/erkexzcx/saurida-fuel-prices/main/prices.json | jq '.alytus_miskininku_g.dyzelinas_b7'
```

## Home Assistant integration

Update `configuration.yml` and add below code:
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
