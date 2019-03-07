#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tidyverse
Version  : 1.2.1
Release  : 12
URL      : https://cran.r-project.org/src/contrib/tidyverse_1.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyverse_1.2.1.tar.gz
Summary  : Easily Install and Load the 'Tidyverse'
Group    : Development/Tools
License  : GPL-3.0
Requires: R-broom
Requires: R-dbplyr
Requires: R-forcats
Requires: R-haven
Requires: R-lubridate
Requires: R-modelr
Requires: R-readr
Requires: R-readxl
Requires: R-reprex
Requires: R-rstudioapi
Requires: R-rvest
Requires: R-tidyr
Requires: R-xml2
BuildRequires : R-broom
BuildRequires : R-dbplyr
BuildRequires : R-forcats
BuildRequires : R-haven
BuildRequires : R-lubridate
BuildRequires : R-modelr
BuildRequires : R-readr
BuildRequires : R-readxl
BuildRequires : R-reprex
BuildRequires : R-rstudioapi
BuildRequires : R-rvest
BuildRequires : R-tidyr
BuildRequires : R-xml2
BuildRequires : clr-R-helpers

%description
because they share common data representations and 'API' design. This
    package is designed to make it easy to install and load multiple
    'tidyverse' packages in a single step. Learn more about the 'tidyverse'

%prep
%setup -q -c -n tidyverse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521269074

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521269074
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyverse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyverse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyverse
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tidyverse|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyverse/DESCRIPTION
/usr/lib64/R/library/tidyverse/INDEX
/usr/lib64/R/library/tidyverse/LICENSE
/usr/lib64/R/library/tidyverse/Meta/Rd.rds
/usr/lib64/R/library/tidyverse/Meta/features.rds
/usr/lib64/R/library/tidyverse/Meta/hsearch.rds
/usr/lib64/R/library/tidyverse/Meta/links.rds
/usr/lib64/R/library/tidyverse/Meta/nsInfo.rds
/usr/lib64/R/library/tidyverse/Meta/package.rds
/usr/lib64/R/library/tidyverse/Meta/vignette.rds
/usr/lib64/R/library/tidyverse/NAMESPACE
/usr/lib64/R/library/tidyverse/NEWS.md
/usr/lib64/R/library/tidyverse/R/tidyverse
/usr/lib64/R/library/tidyverse/R/tidyverse.rdb
/usr/lib64/R/library/tidyverse/R/tidyverse.rdx
/usr/lib64/R/library/tidyverse/doc/index.html
/usr/lib64/R/library/tidyverse/doc/manifesto.Rmd
/usr/lib64/R/library/tidyverse/doc/manifesto.html
/usr/lib64/R/library/tidyverse/help/AnIndex
/usr/lib64/R/library/tidyverse/help/aliases.rds
/usr/lib64/R/library/tidyverse/help/figures/logo.png
/usr/lib64/R/library/tidyverse/help/paths.rds
/usr/lib64/R/library/tidyverse/help/tidyverse.rdb
/usr/lib64/R/library/tidyverse/help/tidyverse.rdx
/usr/lib64/R/library/tidyverse/html/00Index.html
/usr/lib64/R/library/tidyverse/html/R.css
