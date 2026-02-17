# Regel av 72 — Investeringskalkulator

Ein interaktiv kalkulator som viser kor mange år det tar å doble investeringa di, med støtte for månedleg sparing, kapitalskatt og inflasjon.

**Live:** [hornknutsen.github.io/Test1](https://hornknutsen.github.io/Test1/)

---

## Funksjonar

- **Regel av 72** — raskt hoderekningsestimat (`72 / rente`)
- **Eksakt berekning** — logaritmeformel for nøyaktig svar
- **Månedleg sparing** — viser korleis jamleg sparing påverkar veksten
- **Kapitalskatt** — reduserer effektiv avkastning (standard 22%)
- **Inflasjon** — viser realverdi/kjøpekraft over tid
- **Interaktiv graf** — samanliknar nominell, etter-skatt og realverdi

## Bruk

Åpne `index.html` i ein nettlesar, eller besøk den live lenkja over.

Juster sliderane for:

| Parameter | Standard | Område |
|---|---|---|
| Startbeløp | 10 000 kr | 1 000 – 1 000 000 kr |
| Månedleg sparing | 500 kr | 0 – 20 000 kr |
| Årleg rente | 7% | 0,5 – 30% |
| Kapitalskatt | 22% | 0 – 50% |
| Inflasjon | 3% | 0 – 15% |

## Formlar

```
Regel av 72:    år ≈ 72 / rente
Eksakt:         år = log(2) / log(1 + r)
Med sparing:    FV = P·(1+r)ⁿ + PMT·((1+rm)^(12n) − 1) / rm
Etter skatt:    r_netto = r · (1 − skattesats)
Realverdi:      FV_real = FV_netto / (1 + inflasjon)ⁿ
```

## Filer

```
finans-prosjekt/
├── index.html   # Nettsida (HTML, CSS og JavaScript i éi fil)
└── dobling.py   # Python-script for terminalbruk
```

## Python-script

For terminalbruk utan nettlesar:

```bash
python3 dobling.py
```

Scriptet spør om rente og skriv ut estimat (Regel av 72) og eksakt svar.
