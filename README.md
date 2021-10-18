# Introduction

This repo contains some code and data to demonstrate how to work with [snakemake](https://snakemake.readthedocs.io/en/stable/).

# Submit jobs to Slurm

Put the following content to `~/.config/snakemake/{profile_name}/config.yaml`

```yaml
jobs: 60
cluster: "sbatch --nodes=1 --mem={resources.mem} --time={resources.time}"
use-conda: true
default-resources: [time="00:10:00", mem="15G"]
```
