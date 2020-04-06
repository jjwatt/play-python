{ stdenv, fetchurl, python38Packages }:

python38Packages.buildPythonApplication rec {
	pname = "myhy38";
	version = "0.18.0-16-g88f30c4";
	src = ./hy;
	propogatedBuildInputs = with python38Packages; [
		appdirs
		astor
		clint
		colorama
		fastentrypoints
		funcparserlib
		rply
		pygments
		# probably only needed for test
		pytest
		flake8
		# only needed for install
		setuptools
	];
	checkInputs = with python38Packages; [ pytest ];
	meta = with stdenv.lib; {
		description = "A LISP dialect embedded in Python";
		homepage = "http://hylang.org/";
		license = licenses.mit;
		maintainers = with maintainers; [ nixy ];
		platforms = platforms.all;
	};
}
