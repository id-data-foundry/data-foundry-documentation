
# How to build this with Docker

Use the Dockerfile and the command to build the base Docker container for the docs:

```bash

docker build -t df-docs .

```

Then you can start serving the site locally with:

```bash

docker run --rm -p 4000:4000 -v "$(pwd):/usr/src/app" df-docs bundle exec jekyll serve --host 0.0.0.0

```

Once you are happy Then you can start building and rebuilding the site with:

```bash

docker run --rm -v "$PWD:/usr/src/app" df-docs bundle exec jekyll build

```

--

This documentation site is build with [Jekyll](https://jekyllrb.com) and [Just the Docs](https://just-the-docs.github.io/just-the-docs/) licensed as [MIT License](https://en.wikipedia.org/wiki/MIT_License)

