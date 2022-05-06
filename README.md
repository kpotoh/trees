# Nwk2json

[file](https://gist.github.com/jhcepas/9205262)

## Workflow

```bash
seq 10 | parallel nw_gen -d {} '>' random_d{}.tre

ls random_d*.tre | parallel echo {} ';' nw_stats {} ';' echo

seq 12 | parallel echo {} ';' python src/from_site.py data/random_d{}.tre '>' data/random_d{}.tre.json
```

## Logs

```txt
  502,1 MiB [##########]  random_d12.tre.json
  212,2 MiB [####      ]  random_d11.tre.json
   73,5 MiB [#         ]  random_d10.tre.json
   29,0 MiB [          ]  random_d9.tre.json
    8,8 MiB [          ]  random_d8.tre.json
    4,0 MiB [          ]  random_d7.tre.json
    1,4 MiB [          ]  random_d6.tre.json
  368,0 KiB [          ]  random_d5.tre.json
  112,0 KiB [          ]  random_d4.tre.json
   44,0 KiB [          ]  random_d3.tre.json
   12,0 KiB [          ]  random_d2.tre.json
    4,0 KiB [          ]  random_d1.tre.json
    0,0   B [          ]  random_dseq.tre.json
```

```txt
random_d1.tre
Type:   Phylogram
#nodes: 13
#leaves:        7
#dichotomies:   6
#leaf labels:   7
#inner labels:  5

random_d2.tre
Type:   Phylogram
#nodes: 29
#leaves:        15
#dichotomies:   14
#leaf labels:   15
#inner labels:  13

random_d3.tre
Type:   Phylogram
#nodes: 97
#leaves:        49
#dichotomies:   48
#leaf labels:   49
#inner labels:  47

random_d4.tre
Type:   Phylogram
#nodes: 217
#leaves:        109
#dichotomies:   108
#leaf labels:   109
#inner labels:  107

random_d5.tre
Type:   Phylogram
#nodes: 583
#leaves:        292
#dichotomies:   291
#leaf labels:   292
#inner labels:  290

random_d10.tre
Type:   Phylogram
#nodes: 66615
#leaves:        33308
#dichotomies:   33307
#leaf labels:   33308
#inner labels:  33306

random_d6.tre
Type:   Phylogram
#nodes: 1915
#leaves:        958
#dichotomies:   957
#leaf labels:   958
#inner labels:  956

random_d7.tre
Type:   Phylogram
#nodes: 4819
#leaves:        2410
#dichotomies:   2409
#leaf labels:   2410
#inner labels:  2408

random_d8.tre
Type:   Phylogram
#nodes: 9949
#leaves:        4975
#dichotomies:   4974
#leaf labels:   4975
#inner labels:  4973

random_d9.tre
Type:   Phylogram
#nodes: 28037
#leaves:        14019
#dichotomies:   14018
#leaf labels:   14019
#inner labels:  14017

random_d11.tre
Type:   Phylogram
#nodes: 178115
#leaves:        89058
#dichotomies:   89057
#leaf labels:   89058
#inner labels:  89056

random_d12.tre
Type:   Phylogram
#nodes: 393495
#leaves:        196748
#dichotomies:   196747
#leaf labels:   196748
#inner labels:  196746
```
