# Python Business Rules Engine (ZEN Engine)

ZEN Engine is a cross-platform, Open-Source Business Rules Engine (BRE). It is written 
in Rust and provides native bindings for NodeJS and Python. ZEN Engine allows to load and 
execute [JSON Decision Model (JDM)](https://gorules.io/docs/rules-engine/json-decision-model) from JSON files.

![GoRules JSON Decision Model](./images/zen-engine-screenshot1.png)

An open-source React editor is available on our [JDM Editor](https://github.com/gorules/jdm-editor) repo.

## Files

Modify the default files to get started with your own project.

* `README.md` -- This project's readme in Markdown format.
* `cdsw-build.sh` -- A custom build script used for models and experiments. This
will pip install our dependencies, primarily the scikit-learn library.
* `zen-rules-engine-api.py` -- A simple API wrapper for loading the JSON Decision Model (JDM) files and runing REST json requests against it.
* `rule-rngine-jdm-files` --  A folder repository the contains the JSON Decision Model (JDM) files for different rules engine
* `images` -- A folder containing images used in the README document


## Instructions for Launching the Rule Engine as an API REST service
1. Click "Models" -> "Create New Model".
2. Give the model a name and description and select the authentication type for the REST service API
3. Under the "Build" section, select the file zen-rules-engine-api.py
4. For the function provide the api entry point function name of zen-api from the zen-rules-engine-api.py file
5. Provide a sample JSON input, for example:
```
{
  "customer": {
    "country": "US"
  },
  "cart": {
    "total": 1500
  }
}
```
6. Launch the model

![CML Create Model](./images/launch-model-screenshot1.png)