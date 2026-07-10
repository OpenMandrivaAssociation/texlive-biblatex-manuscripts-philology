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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds a new entry type: @manuscript to manage manuscript in
classical philology, for example to prepare a critical edition.

