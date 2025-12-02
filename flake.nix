{
  description = "flake with FHS environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        fhs = pkgs.buildFHSEnv {
          name = "advent-of-code";
          # targetPkgs =
          #   ps: with ps; [
          #   ];
          # multiPkgs = ps: with ps; [ ]; # 32-bit libs
          runScript = "bash";
        };
      in
      {
        devShells.default = fhs.env;
      }
    );
}
