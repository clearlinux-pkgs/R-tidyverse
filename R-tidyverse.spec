#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tidyverse
Version  : 2.0.0
Release  : 49
URL      : https://cran.r-project.org/src/contrib/tidyverse_2.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyverse_2.0.0.tar.gz
Summary  : Easily Install and Load the 'Tidyverse'
Group    : Development/Tools
License  : MIT
Requires: R-broom
Requires: R-cli
Requires: R-conflicted
Requires: R-dbplyr
Requires: R-dplyr
Requires: R-dtplyr
Requires: R-forcats
Requires: R-ggplot2
Requires: R-googledrive
Requires: R-googlesheets4
Requires: R-haven
Requires: R-hms
Requires: R-httr
Requires: R-jsonlite
Requires: R-lubridate
Requires: R-magrittr
Requires: R-modelr
Requires: R-pillar
Requires: R-purrr
Requires: R-ragg
Requires: R-readr
Requires: R-readxl
Requires: R-reprex
Requires: R-rlang
Requires: R-rstudioapi
Requires: R-rvest
Requires: R-stringr
Requires: R-tibble
Requires: R-tidyr
Requires: R-xml2
BuildRequires : R-broom
BuildRequires : R-cli
BuildRequires : R-conflicted
BuildRequires : R-dbplyr
BuildRequires : R-dplyr
BuildRequires : R-dtplyr
BuildRequires : R-forcats
BuildRequires : R-ggplot2
BuildRequires : R-googledrive
BuildRequires : R-googlesheets4
BuildRequires : R-haven
BuildRequires : R-hms
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-lubridate
BuildRequires : R-magrittr
BuildRequires : R-mockr
BuildRequires : R-modelr
BuildRequires : R-pillar
BuildRequires : R-purrr
BuildRequires : R-ragg
BuildRequires : R-readr
BuildRequires : R-readxl
BuildRequires : R-reprex
BuildRequires : R-rlang
BuildRequires : R-rstudioapi
BuildRequires : R-rvest
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-xml2
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
because they share common data representations and 'API' design. This
    package is designed to make it easy to install and load multiple
    'tidyverse' packages in a single step. Learn more about the

%prep
%setup -q -n tidyverse
cd %{_builddir}/tidyverse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677085623

%install
export SOURCE_DATE_EPOCH=1677085623
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyverse/CITATION
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
/usr/lib64/R/library/tidyverse/doc/paper.R
/usr/lib64/R/library/tidyverse/doc/paper.Rmd
/usr/lib64/R/library/tidyverse/doc/paper.html
/usr/lib64/R/library/tidyverse/help/AnIndex
/usr/lib64/R/library/tidyverse/help/aliases.rds
/usr/lib64/R/library/tidyverse/help/figures/logo.png
/usr/lib64/R/library/tidyverse/help/paths.rds
/usr/lib64/R/library/tidyverse/help/tidyverse.rdb
/usr/lib64/R/library/tidyverse/help/tidyverse.rdx
/usr/lib64/R/library/tidyverse/html/00Index.html
/usr/lib64/R/library/tidyverse/html/R.css
/usr/lib64/R/library/tidyverse/tests/testthat.R
/usr/lib64/R/library/tidyverse/tests/testthat/_snaps/attach.md
/usr/lib64/R/library/tidyverse/tests/testthat/_snaps/conflicts.md
/usr/lib64/R/library/tidyverse/tests/testthat/_snaps/logo.md
/usr/lib64/R/library/tidyverse/tests/testthat/test-attach.R
/usr/lib64/R/library/tidyverse/tests/testthat/test-conflicts.R
/usr/lib64/R/library/tidyverse/tests/testthat/test-logo.R
/usr/lib64/R/library/tidyverse/tests/testthat/test-utils.R
