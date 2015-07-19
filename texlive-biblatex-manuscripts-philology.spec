# revision 33195
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-manuscripts-philology
# catalog-date 2014-03-15 23:38:06 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-biblatex-manuscripts-philology
Version:	1.1.0
Release:	5
Summary:	Manage classical manuscripts with biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-manuscripts-philology
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-manuscripts-philology.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-manuscripts-philology.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds a new entry type: @manuscript to manage
manuscript in classical philology, for example to prepare a
critical edition.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/english-manuscripts.lbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/french-manuscripts.lbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts.bbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts.dbx
%doc %{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/README
%doc %{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/example.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/example.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/example.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/makefile
%doc %{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
