
# Styleguide for DF documentation

Write fluent English prose with bullets where necessary and plenty of links to other parts of the documentation. We target an audience of beginning learners, creative technologists with specific questions and needs, and more advanced Data Foundry users who would like to look something up. Some more specific guides follow:

- Headings should be short and expressive, they do not end with punctuation.
- `index.md` files provide the overview over sections of this documentation site; they point at their children with short explanations.
- Content is organized in folders; folder names are in CamelCase and do not contain whitespace or are prefixed with numbers.
- Ordering of items in a section / folder is done by `nav_order` in the file preamble.
- All links use Liquid embedding, so we can let Jekyll check broken links automatically. This includes images, too.
- Unless in code or the platform, it's "Data Foundry", two words, capitalized.

--

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

