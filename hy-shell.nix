# simple python shell to get started
#{ pkgs ? import <nixpkgs> {} }:
#with pkgs;
with import <nixpkgs> {};
let
	pythonEnv = python38.withPackages (ps: [
		ps.ipython
		ps.ipdb
		ps.appdirs
		ps.astor
		ps.colorama
		ps.clint
		ps.fastentrypoints
		ps.funcparserlib
		ps.rply
		ps.pytest
		ps.flake8
		ps.pygments
		ps.setuptools
	]);
in mkShell {
	buildInputs = [
		pythonEnv
	];
}

