# { pkgs ? import <nixpkgs> {} }:

# pkgs.mkShell {
#   buildInputs = [
#     pkgs.texlive.combined.scheme-full
#     pkgs.biber
#     pkgs.gnumake
#   ];
# }

# buildInputs = with pkgs.texlive; [
  #   # General Tools
  #   combined.scheme-full

  #   # Specific Packages
  #   babel
  #   csquotes
  #   dirtytalk
  #   fontenc
  #   geometry
  #   glossaries
  #   graphicx
  #   hyperref
  #   inputenc
  #   listings
  #   multicol
  #   multirow
  #   scrlayer-scrpage
  #   setspace
  #   tocbasic

  #   # Biber and Biblatex for bibliography management
  #   biber
  #   biblatex

  #   # Utilities
  #   latexmk
  # ];