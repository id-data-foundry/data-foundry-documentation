source 'https://rubygems.org'

gem "jekyll", "~> 4.4.1"
gem "bigdecimal"

gem "just-the-docs", "0.12.0"
gem "jekyll-sass-converter", "~> 2.0"

# short links to different pages as a way to migrate from the old documentantion
gem 'jekyll-redirect-from'

# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
# gem "github-pages", group: :jekyll_plugins
# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

gem "jekyll-sitemap"

# link checking: https://www.supertechcrew.com/jekyll-check-for-broken-links/
gem 'rake'
gem 'html-proofer'