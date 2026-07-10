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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/auto-pst-pdf
%dir %{_datadir}/texmf-dist/source/latex/auto-pst-pdf
%dir %{_datadir}/texmf-dist/tex/latex/auto-pst-pdf
%doc %{_datadir}/texmf-dist/doc/latex/auto-pst-pdf/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/auto-pst-pdf/auto-pst-pdf.pdf
%doc %{_datadir}/texmf-dist/doc/latex/auto-pst-pdf/example-psfrag.tex
%doc %{_datadir}/texmf-dist/doc/latex/auto-pst-pdf/example.eps
%doc %{_datadir}/texmf-dist/doc/latex/auto-pst-pdf/example.tex
%doc %{_datadir}/texmf-dist/source/latex/auto-pst-pdf/auto-pst-pdf.dtx
%doc %{_datadir}/texmf-dist/source/latex/auto-pst-pdf/auto-pst-pdf.ins
%{_datadir}/texmf-dist/tex/latex/auto-pst-pdf/auto-pst-pdf.sty
