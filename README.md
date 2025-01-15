## Setup

```sh
git clone https://github.com/m0nK3man/elastalert-docker-compose.git elastalert
cd elastalert
mkdir ca
mkdir rules
```

Put your elasticsearch certs in the ca/ folder, these will be use to connect to elasticsearch

Your custom rules will go in the rules/ folder

The directory should look like this:
```
.
├── ca
│   ├── ca.crt
│   └── ca.key
├── config.yaml
├── docker-compose.yml
├── example_rules
│   ├── elastalert-to-telegram.yaml
│   ├── example_cardinality.yaml
│   ├── example_change.yaml
│   ├── example_frequency.yaml
│   ├── example_new_term.yaml
│   ├── example_opsgenie_frequency.yaml
│   ├── example_percentage_match.yaml
│   ├── example_single_metric_agg.yaml
│   ├── example_spike_single_metric_agg.yaml
│   ├── example_spike.yaml
│   ├── jira_acct.txt
│   ├── ssh-repeat-offender.yaml
│   └── ssh.yaml
├── README.md
└── rules
    └── test.yaml
```

### Usage
Change the compose env to point to your ELK stack, if needed to change the port, modify the config.yaml file, then run:
```sh
docker compose up -d
```
