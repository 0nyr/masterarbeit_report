{
  description = "Python and LaTeX environment for my thesis.";

  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;
    flake-utils.url = github:numtide/flake-utils;
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python311Packages;
      in
      {
        devShells.default = pkgs.mkShell {
          # packages needed to build the environment.
          nativeBuildInputs = with pkgs; [
            # LaTeX
            pkgs.texlive.combined.scheme-full
            pkgs.biber
            pkgs.gnumake
            # Adding Java for LTeX spell checker
            pkgs.openjdk
          ];

          # package needed at build and runtime.
          buildInputs = with pkgs; [
            # the environment.
            pythonPackages.python

            # testing
            pythonPackages.pytest

            # LaTeX
            pythonPackages.pygments

            # python packages
            pythonPackages.numpy
            pythonPackages.tqdm
            pythonPackages.graphviz
            pythonPackages.pygraphviz
            pythonPackages.pydot # needed with networkx
            pythonPackages.networkx
            pythonPackages.pandas
            pythonPackages.seaborn
            pythonPackages.matplotlib
            pythonPackages.jinja2
          ];
        };
      }
    );
}
