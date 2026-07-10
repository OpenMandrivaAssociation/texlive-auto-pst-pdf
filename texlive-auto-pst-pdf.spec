%global tl_name auto-pst-pdf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Wrapper for pst-pdf (with some psfrag features)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/auto-pst-pdf
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(ifplatform)
Requires:	texlive(iftex)
Requires:	texlive(xkeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses --shell-escape to execute pst-pdf when necessary. This
makes it especially easy to integrate into the workflow of an editor
with just "LaTeX" and "pdfLaTeX" buttons. Wrappers are provided for
various psfrag-related features so that Matlab figures via laprint,
Mathematica figures via MathPSfrag, and regular psfrag figures can all
be input consistently and easily.

