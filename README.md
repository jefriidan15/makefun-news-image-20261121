# Saturday 21 November 2026: The World in One Day

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/jefriidan15/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/jefriidan15/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A newspaper front page summing up the world's news of Saturday 21 November 2026 in a single 1024x1024 image, drawn programmatically with PIL.

## The day's stories

Four main panels, one story each:

- **Mexico captures cartel boss** — forces seized FBI most-wanted Fausto Isidro Meza Flores, "El Chapo Isidro", in Guasave, Sinaloa; 11 killed in the violence after.
- **Missile hits Zelenskyy's hometown** — a Russian ballistic missile struck central Kryvyi Rih; 2 killed, about 60 wounded. Ukraine reported 3 missiles and 148 drones overnight, 117 shot down.
- **AI sell-off hits markets** — Wall Street's S&P 500 fell 3.7% on Friday as the AI stock sell-off spread; Japan's Nikkei fell 5.06%.
- **COP31 talks run into overtime** — UN climate talks in Antalya, Turkey, ran past their Friday deadline; fossil fuels went unmentioned in the draft deal.

A strip along the bottom carries five more items from the day: Iran strikes 3 tankers near Hormuz, Nvidia halts H200 AI chip exports to China, Brazil's bacteria-carrying mosquitoes cut dengue cases by 69%, heavy fighting in Haiti, and the death of Phumzile Mlambo-Ngcuka at 71.

## How it works

`entry.png` is the finished front page. `main.py` (Python 3.13, standard library only) copies it to `$MAKEFUN_OUTPUT_DIR/entry.png` and verifies the copy: PNG magic bytes, sha256 digest, and byte-for-byte equality with the source. It runs with no network and writes identical bytes on every run.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Entered on [make.fun](https://make.fun/?ref=2hsnx8we&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
