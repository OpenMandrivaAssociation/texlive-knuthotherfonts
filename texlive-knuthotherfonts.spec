# revision 13293
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-knuthotherfonts
Version:	20111103
Release:	1
Summary:	TeXLive knuthotherfonts package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuthotherfonts.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive knuthotherfonts package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/committee/font1.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/committee/font1base.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/halftone/aphalf.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/halftone/ddhalf.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/halftone/ddralf.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/halftone/halftone.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/halftone/imhalf.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/halftone/imralf.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/mfbook/logobase.mf
%{_texmfdistdir}/fonts/source/public/knuthotherfonts/mfbook/metafon.mf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
