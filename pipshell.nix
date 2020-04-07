with import <nixpkgs> { };

let
  pythonPackages = python3Packages;
in pkgs.mkShell rec {
  name = "impurePythonEnv";
  venvDir = "./.venv";
  buildInputs = with pythonPackages; [
    # A python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    python

    # This execute some shell code to initialize a venv in $venvDir before
    # dropping into the shell
    venvShellHook

    # Those are dependencies that we would like to use from nixpkgs, which will
    # add them to PYTHONPATH and thus make them accessible from within the venv.
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
  ] ++ [ zlib openssl libxml2 git libxslt libzip ];

  # Now we can execute any commands within the virtual environment.
  # This is optional and can be left out to run pip manually.
  # postShellHook = ''
  #   pip install -r requirements.txt
  # '';
}

