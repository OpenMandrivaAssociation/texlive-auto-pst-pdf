Name:		texlive-auto-pst-pdf
Version:	56596
Release:	2
Summary:	Wrapper for pst-pdf (with some psfrag features)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/auto-pst-pdf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses --shell-escape to execute pst-pdf when
necessary. This makes it especially easy to integrate into the
workflow of an editor with just "LaTeX" and "pdfLaTeX" buttons.
Wrappers are provided for various psfrag-related features so
that Matlab figures via laprint, Mathematica figures via
MathPSfrag, and regular psfrag figures can all be input
consistently and easily.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/auto-pst-pdf
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf
#- source
%doc %{_texmfdistdir}/source/latex/auto-pst-pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
