# revision 13293
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-knuthotherfonts
Version:	20111103
Release:	10
Summary:	TeXLive knuthotherfonts package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuthotherfonts.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive knuthotherfonts package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 753007
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718781
- texlive-knuthotherfonts
- texlive-knuthotherfonts
- texlive-knuthotherfonts
- texlive-knuthotherfonts

