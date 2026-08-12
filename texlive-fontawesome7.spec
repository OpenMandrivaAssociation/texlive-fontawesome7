%global tl_name fontawesome7
%global tl_revision 79928
%global tl_version 7.3.1~1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Font Awesome 7 with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fontawesome7
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome7.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome7.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX support for the included Font Awesome 7 Free
icon set. These icons were designed by Fort Awesome and released under
the SIL OFL 1.1 license. The commercial Pro version has only preliminary
alpha support for now, if it is installed and XeLaTeX or LuaLaTeX is
used. For this font you need a paid license, for more information visit
Fort Awesome Pro. More information about Font Awesome is available at
Fort Awesome. To use an icon after the package is loaded, just enter the
name of the icon in CamelCase prefixed with \fa, for example
\faAddressBook for the address-book icon. The TeX files are derived from
the Font Awesome 5package, are maintained by Daniel Nagel and are
released under the LaTeX Project Public License version 1.3c. All
included fonts are provided by Fort Awesome under the SIL OFL 1.1
license. This package is not an official Fort Awesome project. For bug
reports, please open an issue at https://github.com/braniii/fontawesome.

