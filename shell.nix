{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "jekyll-ruby-python-env";

  buildInputs = [
    pkgs.ruby_3_3
    pkgs.bundler
    pkgs.jekyll
    pkgs.python3
    pkgs.python3Packages.pip
  ];

  shellHook = ''
    echo "Jekyll + Ruby + Python environment ready!"
    echo "Ruby: $(ruby --version)"
    echo "Python: $(python3 --version)"
  '';
}
