# Docs
This folder contains the documents I wrote for the exam.

- 📁 [report](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/docs/report)
  - Latex source of lab report. See below for building instructions.
- 📁 [speech](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/docs/speech)
  - Presentation for oral exam.

## Building latex source
1) Setup environment variables for private data: copy the `.env.template`  file
   and update it with the correct data.
   ```bash
   cp report/.env.template report/.env
   ```
2) `cd` to repository root directory and run
   ```bash
   pipenv run build:report
   ```
   to compile latex files once, or
   ```bash
   pipenv run watch:report
   ```
   to build latex on file change.
3) Hope you have all the needed dependencies. Otherwise, `tlmgr` is your
   friend :).
4) The pdf file will be generated in the `build` folder.
