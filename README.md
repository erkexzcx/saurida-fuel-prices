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
  - scan_interval: 3600 # 1 hours
    resource: "https://raw.githubusercontent.com/erkexzcx/saurida-fuel-prices/main/prices.json"
    sensor:
      - name: "Saurida Alytus, Miškininkų g. Fuel Prices"
        json_attributes_path: '$.alytus_miskininku_g'
        value_template: "0"
        json_attributes:
          # Only add fields that are non-zero (exists)
          - dyzelinas_b7
          - benzinas_a95_e5
          - dyzelinas_dz
```

Then you can create a panel like this:
```yaml
type: entity
entity: sensor.saurida_alytus_miskininku_g_fuel_prices
name: Saurida dyzelio kaina/l
unit: €
icon: mdi:gas-station
attribute: dyzelinas_b7
```

Here is how it looks in Home Assistant:

![](https://github.com/erkexzcx/saurida-fuel-prices/raw/main/screenshots/screenshot1.png)

![](https://github.com/erkexzcx/saurida-fuel-prices/raw/main/screenshots/screenshot2.png)
