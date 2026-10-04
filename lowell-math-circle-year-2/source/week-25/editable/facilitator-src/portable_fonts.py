"""Find installed release fonts without bundling third-party binaries."""
from pathlib import Path
import os,subprocess
from reportlab import rl_config

def font_directory(family, filenames, env):
    roots=[Path(os.environ[env])] if os.environ.get(env) else []
    roots += [Path(p) for p in rl_config.TTFSearchPath]
    try:
        found=subprocess.run(['fc-match','-f','%{file}',family],check=True,capture_output=True,text=True).stdout
        if found: roots.append(Path(found).parent)
    except (FileNotFoundError,subprocess.CalledProcessError): pass
    roots += [Path.home()/'.fonts',Path.home()/'Library'/'Fonts',Path('/Library/Fonts')]
    if os.environ.get('WINDIR'): roots.append(Path(os.environ['WINDIR'])/'Fonts')
    directory=next((d for d in roots if all((d/f).is_file() for f in filenames)),None)
    if directory is None: raise FileNotFoundError('Install '+family+' with files '+', '.join(filenames)+', or set '+env+' to their directory.')
    return directory
