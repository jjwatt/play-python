{ stdenv, fetchurl, python38Packages }:

python38Packages.buildPythonApplication rec {
	pname = "hy";
	version = "0.18.0";
	src = python38Packages.fetchPypi {
    inherit pname version;
    sha256 = "04dfwm336gw61fmgwikvh0cnxk682p19b4w555wl5d7mlym4rwj2";
  };

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
	# checkInputs = with python38Packages; [ pytest ];
	meta = with stdenv.lib; {
		description = "A LISP dialect embedded in Python";
		homepage = "http://hylang.org/";
		license = licenses.mit;
		maintainers = with maintainers; [ nixy ];
		platforms = platforms.all;
	};
}
