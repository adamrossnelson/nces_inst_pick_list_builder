# NCES Based Institutional Pick List Builder

Code that can efficiently build pick list of NCES IPEDS listed institutions of higher education. Uses data from NCES.

## Overview, Explanation, Use Case(s)

Provided as a feature by many popular survey software tools a "drill down question" can make it easier for survey respondents to provide reliable data. From Qualtrics.com:

> Respondents first pick from a general drop-down list and from their answers are presented with specific follow-up lists to “drill down” to their answer.

More information about Drill Down questions and use cases:

* [Qualtrics.com](https://www.qualtrics.com/support/survey-platform/survey-module/editing-questions/question-types-guide/specialty-questions/drill-down/)
* [SurveyMonkey.com](https://help.smapply.io/hc/en-us/articles/115001421974-Drill-Down-Question)
* [SoGoSurvey.com](https://www.sogosurvey.com/help/advance-survey-question-types/)

## Components

This routine is provided in the following two computer languages.

* `First add of nces_inst_pick_list_builder.do` runs in Stata (reverse compatible to Stata 13). Collects online from NCES higher educational institutional directory information. Then writes to the current working directory files that are suitable for use in configuging drill down pick list questions at popular survey software providers.
* `First add of nces_inst_pick_list_builder.py` runs in Python 3.6.2. Collects online from NCES higher educational institutional directory information. Then writes to the current working directory files that are suitable for use in configuging drill down pick list questions at popular survey software providers.

## Suggested Citation

Nelson, Adam R. (2017). NCES Based Institutional Pick List Builder. GitHub Repository, https://github.com/adamrossnelson/nces_inst_pick_list_builder DOI: 10.5281/zenodo.3370695
