#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-polyCub
Version  : 0.7.1
Release  : 10
URL      : https://cran.r-project.org/src/contrib/polyCub_0.7.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/polyCub_0.7.1.tar.gz
Summary  : Cubature over Polygonal Domains
Group    : Development/Tools
License  : GPL-2.0
Requires: R-polyCub-lib = %{version}-%{release}
Requires: R-sp
BuildRequires : R-sp
BuildRequires : buildreq-R

%description
# polyCub <img src="man/figures/logo.png" align="right" alt="" width="120" />
The [R](https://www.r-project.org/) package **polyCub** implements
*cubature* (numerical integration) over *polygonal* domains.
It solves the problem of integrating a continuously differentiable
function f(x,y) over simple closed polygons.

%package lib
Summary: lib components for the R-polyCub package.
Group: Libraries

%description lib
lib components for the R-polyCub package.


%prep
%setup -q -c -n polyCub

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549596574

%install
export SOURCE_DATE_EPOCH=1549596574
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polyCub
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polyCub
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polyCub
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library polyCub|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/polyCub/CITATION
/usr/lib64/R/library/polyCub/DESCRIPTION
/usr/lib64/R/library/polyCub/INDEX
/usr/lib64/R/library/polyCub/Meta/Rd.rds
/usr/lib64/R/library/polyCub/Meta/features.rds
/usr/lib64/R/library/polyCub/Meta/hsearch.rds
/usr/lib64/R/library/polyCub/Meta/links.rds
/usr/lib64/R/library/polyCub/Meta/nsInfo.rds
/usr/lib64/R/library/polyCub/Meta/package.rds
/usr/lib64/R/library/polyCub/Meta/vignette.rds
/usr/lib64/R/library/polyCub/NAMESPACE
/usr/lib64/R/library/polyCub/NEWS.md
/usr/lib64/R/library/polyCub/R/polyCub
/usr/lib64/R/library/polyCub/R/polyCub.rdb
/usr/lib64/R/library/polyCub/R/polyCub.rdx
/usr/lib64/R/library/polyCub/R/sysdata.rdb
/usr/lib64/R/library/polyCub/R/sysdata.rdx
/usr/lib64/R/library/polyCub/doc/index.html
/usr/lib64/R/library/polyCub/doc/polyCub.R
/usr/lib64/R/library/polyCub/doc/polyCub.Rmd
/usr/lib64/R/library/polyCub/doc/polyCub.html
/usr/lib64/R/library/polyCub/help/AnIndex
/usr/lib64/R/library/polyCub/help/aliases.rds
/usr/lib64/R/library/polyCub/help/figures/logo.png
/usr/lib64/R/library/polyCub/help/paths.rds
/usr/lib64/R/library/polyCub/help/polyCub.rdb
/usr/lib64/R/library/polyCub/help/polyCub.rdx
/usr/lib64/R/library/polyCub/html/00Index.html
/usr/lib64/R/library/polyCub/html/R.css
/usr/lib64/R/library/polyCub/include/polyCubAPI.h
/usr/lib64/R/library/polyCub/tests/test-all.R
/usr/lib64/R/library/polyCub/tests/testthat/polyiso_powerlaw.c
/usr/lib64/R/library/polyCub/tests/testthat/test-NWGL.R
/usr/lib64/R/library/polyCub/tests/testthat/test-polyCub.R
/usr/lib64/R/library/polyCub/tests/testthat/test-polyiso.R
/usr/lib64/R/library/polyCub/tests/testthat/test-regression.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/polyCub/libs/polyCub.so
/usr/lib64/R/library/polyCub/libs/polyCub.so.avx2
/usr/lib64/R/library/polyCub/libs/polyCub.so.avx512
