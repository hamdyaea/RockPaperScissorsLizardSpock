# Rock Paper Scissors Lizard Spock

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A modern Python 3/Tkinter implementation of the five-choice game. The ten winning combinations are encoded in one reusable rule engine, with unit tests for every pair. The computer uses `secrets.choice`; the GUI displays scores and supports reset.

```sh
python3 LizardSpock.py
python3 LizardSpock.py --choice Rock
python3 -m unittest discover -s tests -v
```

No third-party Python packages are required. The historical implementation is preserved on the [old branch](https://github.com/hamdyaea/RockPaperScissorsLizardSpock/tree/old).
