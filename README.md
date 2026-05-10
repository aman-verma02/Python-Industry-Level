## High-Level Structure

### Here’s a real industry-style ML repo:


ml_project/
│
├── data/                # raw + processed data
├── notebooks/           # experiments (NOT production)
├── src/                 # main source code
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── pipelines/
│   ├── utils/
│
├── config/              # configs (YAML/JSON)
├── tests/               # unit tests
├── logs/                # logs
├── models/              # saved models
├── main.py              # entry point
├── requirements.txt
└── README.md




## Industry Design Principles
1. Separation of Concerns
    * Each module does ONE thing
2. Reproducibility
    * config files
    * versioned data
3. Scalability
    * modular code
    * plug-and-play models
4. Debugging
    * logs
    * small functions


## Good repo = Organized + Modular + Scalable + Reproducible + Debugging + Testable + Documentation + CI/CD 