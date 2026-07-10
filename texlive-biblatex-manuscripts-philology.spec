%global tl_name biblatex-manuscripts-philology
%global tl_revision 66977

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.4
Release:	%{tl_revision}.1
Summary:	Manage classical manuscripts with BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-manuscripts-philology
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-manuscripts-philology.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-manuscripts-philology.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds a new entry type: @manuscript to manage manuscript in
classical philology, for example to prepare a critical edition.

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/documentation
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology-example.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/documentation/makefile
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/english-manuscripts.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/french-manuscripts.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/italian-manuscripts.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/latin-manuscripts.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/manuscripts-NewBibliographyString.sty
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/manuscripts-noautoshorthand.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/manuscripts-noautoshorthand.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/manuscripts-shared.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/manuscripts-shared.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/manuscripts.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/manuscripts.dbx
