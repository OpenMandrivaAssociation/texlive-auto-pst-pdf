Name:		texlive-auto-pst-pdf
Version:	0.6
Release:	1
Summary:	Wrapper for pst-pdf (with some psfrag features)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/auto-pst-pdf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package uses --shell-escape to execute pst-pdf when
necessary. This makes it especially easy to integrate into the
workflow of an editor with just "LaTeX" and "pdfLaTeX" buttons.
Wrappers are provided for various psfrag-related features so
that Matlab figures via laprint, Mathematica figures via
MathPSfrag, and regular psfrag figures can all be input
consistently and easily.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/auto-pst-pdf/auto-pst-pdf.sty
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf/README
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf/auto-pst-pdf-DE.pdf
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf/auto-pst-pdf-DE.tex
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf/auto-pst-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf/example-psfrag.tex
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf/example.eps
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf/example.tex
#- source
%doc %{_texmfdistdir}/source/latex/auto-pst-pdf/auto-pst-pdf.dtx
%doc %{_texmfdistdir}/source/latex/auto-pst-pdf/auto-pst-pdf.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
